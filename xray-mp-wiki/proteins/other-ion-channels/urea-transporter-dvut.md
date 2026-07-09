---
title: "Urea Transporter from Desulfovibrio vulgaris (dvUT)"
created: 2026-06-02
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, channel, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature08558]
verified: regex
uniprot_id: P12277
---

# Urea Transporter from Desulfovibrio vulgaris (dvUT)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P12277">UniProt: P12277</a>

<span class="expr-badge">Homo sapiens</span>

## Overview

The [UREA](/xray-mp-wiki/reagents/substrates/urea) transporter from *Desulfovibrio vulgaris* (dvUT) is a bacterial
homologue of mammalian [UREA](/xray-mp-wiki/reagents/substrates/urea) transporters (UTs). It forms a homotrimeric
channel that facilitates rapid and selective [UREA](/xray-mp-wiki/reagents/substrates/urea) permeation across
biological membranes. Each subunit contains a continuous membrane-spanning
pore with a constricted selectivity filter that coordinates dehydrated [UREA](/xray-mp-wiki/reagents/substrates/urea)
molecules through hydrogen bonding with oxygen ladder residues. The structure
establishes that [UREA](/xray-mp-wiki/reagents/substrates/urea) transporters operate by a channel-like mechanism rather
than a carrier-mediated alternating-access mechanism.


## Publications

### doi/10.1038##nature08558

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3b6r">3B6R</a></td>
      <td>2.3</td>
      <td>P65</td>
      <td>Full-length dvUT (residues 1-334) with N-terminal His6-SUMO tag</td>
      <td>N,N'-dimethylurea (DMU)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: N-terminal His6-SUMO-dvUT fusion (Smt3 system)
- **Notes**: Expressed using pET-SUMO plasmid with N-terminal polyhistidine tag and SUMO domain. Solubilized with 30 mM [DDM](/xray-mp-wiki/reagents/detergents/ddm).

**Purification:**

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: His6-SUMO-dvUT fusion

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
      <td>Cell lysis and solubilization</td>
      <td>Cell disruption</td>
      <td>—</td>
      <td>30 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td>Cells resuspended and solubilized in 30 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
    </tr>
    <tr>
      <td>Cobalt affinity chromatography</td>
      <td>IMAC</td>
      <td>Cobalt affinity column (Clontech)</td>
      <td>30 mM <a href="/xray-mp-wiki/reagents/detergents/ddm">DDM</a></td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag">Polyhistidine Tag (His6)</a> captured on cobalt column</td>
    </tr>
    <tr>
      <td>Tag cleavage</td>
      <td>Proteolytic cleavage</td>
      <td>—</td>
      <td></td>
      <td>His tag and SUMO domain cleaved with SUMO protease</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>Gel filtration</td>
      <td>Superdex 200 10/300 GL</td>
      <td>300 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a> + 40 mM <a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-maltoside">OM</a> (OM)</td>
      <td></td>
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
      <td>8 mg/ml in 300 mM NaCl, 20 mM <a href="/xray-mp-wiki/reagents/buffers/hepes">HEPES</a> pH 7.5, 5 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a>, 40 mM OM</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>22% <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a>1500, 100 mM sodium <a href="/xray-mp-wiki/reagents/buffers/cacodylate">Cacodylate (Sodium Dimethylarsenate)</a> pH 6.5</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>61</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Gradually increased <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a>1500 to 45% over 30 h</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Native crystals in P31 space group (3.8 A). Heavy atom derivatives (Hg, Au) in P65 space group with improved resolution to 2.3 A. DMU-bound crystals obtained by incubating protein with 10 mM DMU at 20 C for 30 min before crystallization.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Channel-like mechanism of urea transport

The dvUT structure reveals a continuous solvent-accessible pore running
through each subunit, demonstrating that [UREA](/xray-mp-wiki/reagents/substrates/urea) transporters operate by a
channel-like mechanism rather than a carrier-mediated alternating-access
mechanism. The pore allows dehydrated [UREA](/xray-mp-wiki/reagents/substrates/urea) molecules to permeate in
single file at rates between 10^4 and 10^6 s^-1, consistent with channel
diffusion. This finding resolves a long-standing question about how UTs
achieve rapid and selective [UREA](/xray-mp-wiki/reagents/substrates/urea) permeation.

### Oxygen ladder selectivity filter

The selectivity filter of dvUT contains two linear arrays of oxygen atoms
(oxygen ladders) from backbone and side-chain oxygens of residues in
pore helices (Pa, Pb) and transmembrane helices T3 and T5. These oxygen
ladders provide continuous hydrogen-bond coordination to [UREA](/xray-mp-wiki/reagents/substrates/urea) as it
progresses through the filter, compensating for dehydration energy. The
filter is flanked by phenylalanine side chains that compress it into a
slot-like shape, and valine/leucine residues create a central constriction.
The symmetry of the filter is remarkable: with one exception (Gln24/Glu187
pair), every residue has an identical symmetry-related partner.

### Helix dipole stabilization of urea binding

The alpha-helix dipole of pore helix b (Pb) provides additional
stabilization for [UREA](/xray-mp-wiki/reagents/substrates/urea) binding. The partial negative charge at the C
terminus of the helix compensates for the partial positive charge on [UREA](/xray-mp-wiki/reagents/substrates/urea)
amide nitrogens. This mechanism, previously noted in potassium channels
and chloride transporters, represents a general principle for stabilizing
polar substrates within membrane protein pores.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/n-octyl-beta-d-glucopyranoside/">n-Octyl beta-D-glucopyranoside (OG)</a> — Related maltoside/glucoside detergent used for membrane protein solubilization
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — Another nonionic detergent used for solubilizing membrane proteins
- <a href="/xray-mp-wiki/reagents/substrates/urea/">Urea</a> — Substrate and ligand of the urea transporter
- <a href="/xray-mp-wiki/reagents/ligands/n-n-dimethylurea/">N,N'-Dimethylurea (DMU)</a> — Urea analogue used in structural studies of dvUT
- <a href="/xray-mp-wiki/reagents/protein-tags/sumo-tag/">SUMO Tag</a> — N-terminal fusion tag used in the dvUT expression construct
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">HEPES Buffer</a> — Buffer component (20 mM, pH 7.5) used in purification and crystallization
- <a href="/xray-mp-wiki/reagents/buffers/cacodylate/">Cacodylate Buffer</a> — Buffer (100 mM, pH 6.5) used in crystallization reservoir
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/channel-like-mechanism/">Channel-like Mechanism</a> — Transport mechanism established by the dvUT structure
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol">beta-Mercaptoethanol</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/peg">PEG</a> — Entity mentioned in text
