---
title: "Tlg2 (Cryptococcus thermophilum Qa-SNARE Protein)"
created: 2026-05-26
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.60724]
verified: regex
uniprot_id: G0S539
---

# Tlg2 (Cryptococcus thermophilum Qa-SNARE Protein)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/G0S539">UniProt: G0S539</a>

<span class="expr-badge">Chaetomium thermophilum</span>

## Overview

Tlg2 is a Qa-SNARE protein from the filamentous fungus Cryptococcus thermophilum that functions in membrane trafficking from the endosome to the trans-Golgi network. Tlg2 has a pronounced tendency to form homo-tetramers driven by SNARE motif bundling. When bound to the SM protein [VPS45](/xray-mp-wiki/proteins/vps45), Tlg2 adopts a novel open conformation in which the Habc domain does not pack against the SNARE motif, leaving it free to initiate SNARE complex assembly. [VPS45](/xray-mp-wiki/proteins/vps45) rescues Tlg2 from homo-oligomeric tetramers into stoichiometric 1:1 complexes.

## Publications

### doi/10.7554##eLife.60724

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xmd">6XMD</a></td>
      <td>3.88 A</td>
      <td>P21221</td>
      <td>C. thermophilum Tlg2 (residues 1-310) cytoplasmic domain in complex with Vps45</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6xm1">6XM1</a></td>
      <td>2.80 A</td>
      <td>P212121</td>
      <td>C. thermophilum full-length Tlg2 (residues 1-327) cytoplasmic domain in complex with Vps45</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-Codon Plus (Agilent)
- **Construct**: C. thermophilum Tlg2 (XP_006697074.1 homolog) with N-terminal His7-MBP tags followed by TEV protease cleavage site. Tlg2(1-327) overproduced at 16 C.

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
      <td>Cell lysis</td>
      <td>Pressure homogenization (Emulsiflex-C5)</td>
      <td>--</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 8.0, 150 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a> + --</td>
      <td>Tlg2(1-327)-His7-MBP overproduced in BL21-Codon Plus at 16 C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>His60 Ni Superflow Resin</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 8.0, 50 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + --</td>
      <td>Low salt wash, eluted with 400 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a></td>
    </tr>
    <tr>
      <td>Anion exchange chromatography</td>
      <td>Ion-exchange chromatography</td>
      <td>MonoQ 10/100</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 8.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> + --</td>
      <td>Gradient from 50 mM to 500 mM NaCl</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Protease digestion (TEV protease)</td>
      <td>His60 Ni Superflow (cleaved His7-MBP tags removed)</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 8.0, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 50 mM NaCl + --</td>
      <td>TEV protease cleaved His7-MBP tags overnight at 4 C</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Size-exclusion chromatography</td>
      <td>Not specified</td>
      <td>25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 8.0, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a> + --</td>
      <td>Final purification</td>
    </tr>
  </tbody>
</table>

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
      <td>SUMO tag cleavage (Tlg2 Habc domain, residues 79-200)</td>
      <td>Protease digestion (Ulp1 protease)</td>
      <td>His60 Ni Superflow</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a>, 50 mM NaCl + --</td>
      <td>SUMO tag removed by Ulp1 protease</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion with streak seeding</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Tlg2(1-310)-<a href="/xray-mp-wiki/proteins/vps45">VPS45</a> complex at 4 mg/ml in 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 8.0, 50 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M potassium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a>, 14% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 3350, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>Room temperature</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~3 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Not specified</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>P21221 crystal form with single complex in asymmetric unit. Streak seeded with Tlg2(1-310)-<a href="/xray-mp-wiki/proteins/vps45">VPS45</a> crystals.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Tlg2(1-327)-<a href="/xray-mp-wiki/proteins/vps45">VPS45</a> full-length complex at 4 mg/ml in 25 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 8.0, 50 mM NaCl, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.2 M potassium <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a>, 14% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> 3350, 5 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a></td>
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
      <td>P212121 crystal form with two complexes in asymmetric unit.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Open conformation mechanism of Qa-SNARE clamping

Tlg2 adopts an open conformation when bound to [VPS45](/xray-mp-wiki/proteins/vps45), with the Habc domain making only a limited contact with the SNARE motif at an approximately 45 degree angle. The linker between Habc and SNARE motif is disordered/unfolded, unlike the Munc18-Stx1 complex where this linker forms a short helix packing against the closed Habc-SNARE motif bundle. This demonstrates that Qa-SNARE clamping is a specialized property of Munc18 rather than a general SM protein property.

### Homo-tetramerization through SNARE motif bundling

Tlg2 has a pronounced tendency to form homo-tetramers through SNARE motif bundling, as demonstrated by size-exclusion chromatography and sedimentation velocity analytical ultracentrifugation (33.8 kDa experimental vs 33.6 kDa expected for tetramer). The Habc domain alone sediments as a monomer. This oligomerization is reversible and [VPS45](/xray-mp-wiki/proteins/vps45) can rescue Tlg2 tetramers into 1:1 complexes.


## Cross-References

- <a href="/xray-mp-wiki/proteins/structural-adhesion/vps45/">Vps45 SNARE Protein</a> — Cognate SM protein that forms 1:1 complexes with Tlg2; co-crystallized in PDB entries 6XMD and 6XM1
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Primary buffer (25 mM, pH 8.0) used in all purification and crystallization steps
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer</a> — Crystallization buffer component (0.2 M potassium citrate)
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Stabilizing additive at 5% (w/v) used throughout purification and crystallization
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Used at 400 mM for Ni-affinity elution and at lower concentrations in tag cleavage buffer
- <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">Sodium Chloride (NaCl)</a> — Used at 150 mM in cell lysis buffer and in anion exchange gradient (50-500 mM)
- <a href="/xray-mp-wiki/reagents/additives/peg/">PEG (Polyethylene Glycol)</a> — Crystallization precipitant (PEG 3350, 14% w/v)
- <a href="/xray-mp-wiki/reagents/protein-tags/bril/">BRIL Fusion Protein</a> — Related protein stabilization approach used in membrane protein crystallography
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni-affinity chromatography used for initial purification of His-tagged Tlg2 constructs
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — SEC used for final purification of Tlg2-Vps45 complexes
