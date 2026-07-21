---
title: "AcrA multidrug efflux pump periplasmic protein"
created: 2026-05-28
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1016##j.str.2005.11.015]
verified: agent
uniprot_id: P54300
---

# AcrA multidrug efflux pump periplasmic protein

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P54300">UniProt: P54300</a>

<span class="expr-badge">Vibrio harveyi</span>

## Overview

AcrA is a periplasmic membrane fusion protein from Escherichia coli that partners with the inner membrane RND transporter [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/acrB) and the outer membrane channel TolC to form the AcrAB-TolC tripartite multidrug efflux system. The crystal structure of the stable core construct AcrA(45-312) with quadruple methionine substitution was determined at 2.71 A resolution by multi-wavelength anomalous diffraction (MAD). AcrA adopts an elongated sickle-shaped monomer composed of three domains: a beta-barrel domain, a lipoyl domain, and an alpha-helical hairpin domain. The alpha-helical hairpin exhibits unsuspected conformational flexibility with four distinct orientations captured in the crystal, which has mechanistic significance for coupling AcrA conformations to TolC channel opening.

## Publications

### doi/10.1016##j.str.2005.11.015

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2f1m">2F1M</a></td>
      <td>2.71 A</td>
      <td>C222</td>
      <td>AcrA(45-312) quadruple methionine mutant (F223M/L224M/L287M/L288M)</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: AcrA(26-397) with C-terminal [His Tag](/xray-mp-wiki/reagents/protein-tags/his6-tag) (LEHHHHHH), or AcrA(45-312) with quadruple methionine substitution (F223M/L224M/L287M/L288M)

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
      <td>Sonication of <a href="/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/">E. coli</a> BL21(DE3) cells expressing AcrA(26-397)</td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> (pH 8.0), 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + --</td>
      <td>Cytoplasmic expression of soluble <a href="/xray-mp-wiki/proteins/acra/">AcrA</a> fragment</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography">IMAC</a></td>
      <td>Ni2+ chelation chromatography</td>
      <td>Poros MC (<a href="/xray-mp-wiki/reagents/additives/nickel-nta/">[Ni-NTA</a>](/xray-mp-wiki/reagents/additives/nickel-nta))</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl</a> (pH 8.0), 150 mM NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole">Imidazole</a> + --</td>
      <td><a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His-tag</a>ged AcrA purified from soluble fraction</td>
    </tr>
    <tr>
      <td>Dialysis and concentration</td>
      <td>Dialysis and Amicon <a href="/xray-mp-wiki/methods/purification/ultrafiltration/">ultrafiltration</a></td>
      <td>--</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> (pH 8.0), 150 mM NaCl + --</td>
      <td>Concentrated using Amicon <a href="/xray-mp-wiki/methods/purification/ultrafiltration/">ultrafiltration</a> (MW cutoff 30 kDa; Millipore)</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography">SEC</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a>](/xray-mp-wiki/methods/purification/size-exclusion-chromatography)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200">Superdex 200</a></td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> (pH 8.0) + --</td>
      <td>Purified to homogeneity, concentrated to 30 mg/mL</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>30 mg/mL AcrA(45-312)-4M in 10 mM <a href="/xray-mp-wiki/reagents/buffers/tris">Tris</a> (pH 8.0)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30% MPD, 20 mM MgCl2, 100 mM <a href="/xray-mp-wiki/reagents/buffers/citrate">Citrate Buffer (Sodium Citrate)</a> (pH 5.4), 1 mM TCEP</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>not specified</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Well buffer supplemented with 1 mM <a href="/xray-mp-wiki/reagents/additives/tcep">TCEP</a>, flash cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Space group C222, cell dimensions a=88.7 A, b=100.0 A, c=332.6 A. Four molecules per asymmetric unit, 60% solvent content. Data collected at APS-BM19 and ALS-8.2.2 beamlines. Multi-wavelength <a href="/xray-mp-wiki/methods/structure-determination/multi-wavelength-anomalous-diffraction/">MAD</a> phasing with <a href="/xray-mp-wiki/reagents/additives/selenomethionine">Selenomethionine (SeMet)</a>-labeled protein. 16 Se si<a href="/xray-mp-wiki/reagents/buffers/tes/">tes</a> located with SHELXL, refined with SHARP. R_work 23.7%, R_free 27.5% at 2.71 A resolution.</td>
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
      <td>pH</td>
      <td>5.4</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Mpd: 30 % [precipitant]  
- Magnesium Chloride: 20 mM [salt]  
- Citrate: 100 mM [buffer]  
- Tcep: 1 mM [additive]</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Conformational flexibility of the alpha-helical hairpin domain

Four distinct conformations of AcrA(45-312)-4M were captured in the crystal, providing
evidence for flexibility of the hinge between the alpha-helical hairpin and lipoyl
domain. The greatest variation is between molecules B and C, which differ by ~15 degrees
overall in alpha-helical hairpin orientation and by 21 A at the loop at the tip of
the hairpin. The lipoyl domain superposes with high structural similarity in all four
molecules (rmsd 0.12 A, 66 C-alpha atoms). The alpha-helical hairpin domains alone
also show similarity (rmsd 0.46 A, 51 C-alpha atoms).

The hinge is located at the base of the hairpin, composed of residues 99-106 in helix
1 and residues 169-173 in helix 2. In molecules A and C, this region is underwound,
having a ~200 A pitch that is greater than the 150 A pitch of a canonical alpha-helical
coiled-coil. In molecules B and D, the hinge regions have a nearly canonical coiled-coil
pitch. This flexibility coincides with conformational changes predicted to occur during
opening of the [TolC](/xray-mp-wiki/proteins/tolc) channel by an iris-like mechanism.

In contrast, the homologous protein MexA from Pseudomonas aeruginosa shows essentially
the same conformation in all 13 copies captured in its crystal structure (maximum rmsd
1.17 A, 230 C-alpha atoms). Molecule D of AcrA has nearly the same alpha-helical hairpin
orientation as the one seen in MexA (rmsd 0.85 A, 183 C-alpha atoms).

### Oligomeric state and crystal packing

The four molecules of AcrA(45-312)-4M in the asymmetric unit pack as an apparent
dimer of dimers. Molecules A and B are related by approximate dyad symmetry, as are
molecules C and D; each set of dimers is related by another approximate 2-fold axis.
The alpha-helical hairpin of AcrA has five heptad repeats per helix, longer than the
four heptad repeats of [MexA](/xray-mp-wiki/proteins/mexa). Packing between the two helices resembles canonical knobs-into-holes
packing of hydrophobic side chains in the a and d positions of the heptad repeat.

In addition to parallel associations, extensive antiparallel associations are observed
in the crystallographic packing. For antiparallel association, adjacent equivalent helices
(alpha1 for MexA and alpha2 for AcrA) pack in antiparallel fashion and contribute residues
predominantly at the c and f positions to the interface. This suggests that the propensity
of MFP alpha-helical hairpins to interact homotypically reconciles the observation that
MFPs are monomeric in solution but oligomeric in the high-concentration environment
of crystals.

### Functional residues and interaction domains

The C-terminal region (residues 313-397) of AcrA, removed by proteolysis in the crystallized
construct, is required for association with both the inner membrane RND protein AcrB
and the outer membrane channel TolC. The proteolytically sensitive C-terminal region
is also implicated in conferring association with AcrB.

The beta-barrel domain of AcrA has also been implicated in TolC association, based on
suppressor mutations that restore function in a TolC mutant strain. The stoichiometry
of AcrA remains uncertain, with a trimeric form found in vivo but a monomeric form
in vitro.

Site-directed mutagenesis of hydrophobic residues in the alpha-helical hairpin (F223M/L224M
and L287M/L288M) significantly increased susceptibility to multiple antibiotics and
detergents ([Erythromycin](/xray-mp-wiki/reagents/ligands/erythromycin), novobiocin, ethidium bromide, SDS, puromycin), confirming
that these positions are critical for AcrA function in the efflux system.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB multidrug efflux pump</a> — Inner membrane RND partner in the AcrAB-[TolC](/xray-mp-wiki/proteins/tolc) tripartite efflux system
- <a href="/xray-mp-wiki/proteins/abc-transporters/mexB/">MexB Efflux Pump</a> — P. aeruginosa RND inner membrane partner of MexA, homologous to [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/acrB)
- <a href="/xray-mp-wiki/reagents/additives/selenomethionine/">Selenomethionine (SeMet)</a> — Used for MAD phasing via [Selenomethionine (SeMet)](/xray-mp-wiki/reagents/additives/selenomethionine) labeling of quadruple methionine mutant
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris Buffer</a> — Primary buffer (50 mM [Tris](/xray-mp-wiki/reagents/buffers/tris) pH 8.0) used in expression, purification, and crystallization
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a> — 20 mM [MgCl2](/xray-mp-wiki/reagents/additives/magnesium-chloride) component of crystallization reservoir
- <a href="/xray-mp-wiki/reagents/buffers/citrate/">Citrate Buffer</a> — 100 mM [Citrate Buffer (Sodium Citrate)](/xray-mp-wiki/reagents/buffers/citrate) (pH 5.4) component of crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/mpd/">2-Methyl-2,4-pentanediol (MPD)</a> — 30% [MPD](/xray-mp-wiki/reagents/additives/mpd) used as precipitant in crystallization
- <a href="/xray-mp-wiki/reagents/additives/thermolysin/">Thermolysin</a> — Used for limited proteolytic digestion to map AcrA domain architecture
- <a href="/xray-mp-wiki/proteins/mexa">MexA (P. aeruginosa)</a> — Related membrane protein structure
- <a href="/xray-mp-wiki/proteins/tolc">TolC Outer Membrane Channel</a> — Related membrane protein structure
