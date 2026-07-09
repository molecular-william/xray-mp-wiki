---
title: "LarB (Lactiplantibacillus plantarum)"
created: 2026-05-29
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1021##acs.biochem.3c00242, doi/10.1021##acs.biochem.5b01345]
verified: regex
uniprot_id: F9UST0
---

# LarB (Lactiplantibacillus plantarum)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/F9UST0">UniProt: F9UST0</a>

<span class="expr-badge">Lactobacillus plantarum</span>

## Overview

LarB is an enzyme from Lactiplantibacillus plantarum (formerly Lactobacillus plantarum) that catalyzes the first step in the biosynthesis of the nickel-pincer nucleotide (NPN) cofactor. LarB carboxylates [Nicotinic Acid Adenine Dinucleotide (NaAD)](/xray-mp-wiki/reagents/cofactors/nicotinic-acid-adenine-dinucleotide/) at the C5 position of the pyridinium ring and hydrolyzes the phosphoanhydride bond, producing pyridinium-3,5-biscarboxylic acid mononucleotide ([P2CMN](/xray-mp-wiki/reagents/ligands/pyridinium-3-5-biscarboxylic-acid-mononucleotide/)) and AMP. The enzyme uses CO2 for substrate carboxylation and employs a Cys221 nucleophile for covalent intermediate formation.


## Publications

### doi/10.1021##acs.biochem.3c00242

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/s127a-larb-naad">S127A-LARB-NAAD</a></td>
      <td>2.5</td>
      <td>P212121</td>
      <td>S127A variant with Strep II tag</td>
      <td>NaAD</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3)
- **Construct**: Strep II-tagged LarB

**Purification:**

- **Expression system**: E. coli BL21 (DE3)
- **Expression construct**: Strep II-tagged LarB

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>—</td>
      <td>LB medium with <a href="/xray-mp-wiki/reagents/additives/kanamycin/">Kanamycin</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell lysis</td>
      <td>Sonication</td>
      <td>—</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Strep-Tactin affinity</td>
      <td>Strep-Tactin</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 150 mM NaCl</td>
      <td></td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>—</td>
      <td>100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.5, 150 mM NaCl</td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: 100 mM [Tris-HCl Buffer](/xray-mp-wiki/reagents/buffers/tris/) pH 7.5, 150 mM NaCl

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>~12 mg/mL S127A LarB</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>2 mM nitrilotriacetic acid, 0.7 mM ZnSO4, 100 mM magnesium formate, 10-20% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>25% <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a>, 10 mM NaAD, 10-20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350, 25 mM magnesium formate</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals soaked overnight in 5-10 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> (pH 8), 10 mM NaAD, 10-20% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 3350, 25 mM magnesium formate before cryoprotection. Zn2+ required for crystallization but must be removed for active site substrate binding.</td>
    </tr>
  </tbody>
</table>
### doi/10.1021##acs.biochem.5b01345

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7mj2">7MJ2</a></td>
      <td>2.1</td>
      <td>P212121</td>
      <td>Wild-type with Strep II tag</td>
      <td>NAD+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21 (DE3)
- **Construct**: Strep II-tagged LarB

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>NAD+ soaked into LarB crystals to form LarB-NAD+ complex. Cys221 covalently attaches to C4 of the pyridine ring.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Revised Catalytic Mechanism

The S127A LarB-NaAD structure revealed a revised catalytic mechanism. The carboxylate of
NaAD is oriented in the same manner as the amide of NAD+, pointing away from the metal ion.
The conserved Glu180 residue is improperly positioned to serve as a general base to abstract
the C5 proton (average distance 4.9 A). Instead, Glu180 is within hydrogen bond distance
of the thiol group of Cys221 (3.1-3.4 A), suggesting that Cys221 and Glu180 form a catalytic
dyad that facilitates nucleophilic attack of the thiolate anion on C4 of NaAD. No Cys221-pyridine
ring linkage was observed in the S127A LarB-NaAD structure, unlike the WT LarB-NAD+ structure.

### DaAD Intermediate Trapping

The S127A variant exhibits ~90% reduction in nonproductive NaAD hydrolysis activity compared
to WT LarB, allowing accumulation and identification of the DaAD intermediate by mass
spectrometry. The S127A variant was capable of carboxylating ~75% of the NaAD substrate,
whereas only ~20% was carboxylated by the WT enzyme.

### CO2 Binding Site

A tentative CO2 binding mode was identified in the S127A LarB-NaAD structure. CO2 forms
electrostatic interactions with Mg2+, Arg159, and the hydroxyl and phosphate groups of NaAD.
Arg159, which is essential for LarB activity, uses its flexible long arm to recruit and
hand over CO2 to the bound Mg2+. The Mg2+ bound to NaAD, together with Ala155, Gly156,
and Arg159, forms the entrance of a narrow pathway for CO2 access to C5 of NaAD.


## Cross-References

- <a href="/xray-mp-wiki/reagents/cofactors/nicotinic-acid-adenine-dinucleotide/">NaAD</a> — Authentic substrate of LarB
- <a href="/xray-mp-wiki/reagents/ligands/dinicotinic-acid-adenine-dinucleotide/">DaAD</a> — Reaction intermediate identified by MS
- <a href="/xray-mp-wiki/reagents/ligands/pyridinium-3-5-biscarboxylic-acid-mononucleotide/">P2CMN</a> — Product of LarB-catalyzed reaction
- <a href="/xray-mp-wiki/reagents/ligands/nicotinamide-adenine-dinucleotide/">NAD+</a> — Substrate analogue that covalently binds to Cys221
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/nickel-pincer-nucleotide-cofactor-biosynthesis/">NPN Cofactor Biosynthesis</a> — Pathway initiated by LarB-catalyzed reaction
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/ethylene-glycol/">Ethylene Glycol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/kanamycin/">Kanamycin</a> — Additive used in purification or crystallization buffers
