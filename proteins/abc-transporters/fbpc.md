---
title: "FbpC (Nucleotide-Binding Domain of the FbpABC Iron Transporter)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2009.07.009]
verified: false
---

# FbpC (Nucleotide-Binding Domain of the FbpABC Iron Transporter)

## Overview

FbpC is the nucleotide-binding domain (NBD) of the FbpABC ferric  uptake -binding cassette (ABC) transporter from Neisseria gonorrhoeae. The crystal structure was determined at 1.9 A resolution, revealing a domain-swapped physiological dimer in the asymmetric unit. This represents the first observation of [Three-Dimensional Domain Swapping](/xray-mp-wiki/concepts/structural-mechanisms/domain-swapping/) in ABC importers. The C-terminal regulatory domains of each monomer undergo a substantial domain swap, creating an unusually extended dimer interface with a six-histidine cluster at the base. Molecular dynamics simulations comparing FbpC with the homologous  NBD demonstrated that while FbpC does not open as far or as rapidly as  upon  removal, both closed structures have higher free energies than their respective open states, indicating that  binding free energy is partially stored as strain energy and released following hydrolysis.

## Publications

### doi/10.1016##j.str.2009.07.009

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3fvq">3FVQ</a></td>
      <td>1.9 A</td>
      <td>P 2 2 2</td>
      <td>Full-length FbpC (residues 1-352) from N. gonorrhoeae with C-terminal 6x His-tag; expressed in E. coli BL21(DE3); includes two naturally occurring sequence variants (V147A, F283Y) relative to reference genome AE004969</td>
      <td>, calcium ion</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: FbpC with C-terminal 6x His-tag in pET28a vector; induced with 0.2 mM  at OD600 0.8, growth continued for 3 h at 25 C; SeMet labeling in M9 media with amino acid suppression method

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
      <td>Sonication</td>
      <td>--</td>
      <td>25 mM  pH 8.0, 5 mM , 0.1 mM , 20%  + --</td>
      <td>Resuspended pellet lysed by sonication; centrifuged at 25,000 x g for 30 min at 4 C</td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA silica (Promega) batch binding</td>
      <td>Ni-NTA silica</td>
      <td>25 mM  pH 8.0, 5 mM , 0.5 M NaCl, 20% , 0.05 M  + --</td>
      <td>5 mL Ni-NTA beads incubated with lysate for 1 h at 4 C with 20 mM ; washed with 30 column volumes; eluted with step gradient to 0.25 M </td>
    </tr>
    <tr>
      <td> cobalt-affinity chromatography</td>
      <td> cobalt-affinity resin (BD Biosciences) batch binding</td>
      <td> cobalt-affinity resin</td>
      <td>25 mM  pH 8.0, 5 mM , 0.5 M NaCl, 20% , 30 mM  + --</td>
      <td>Eluted FbpC diluted 1:10 in no- buffer; incubated with 5 mL  resin for 1 h at 4 C; washed with 30 mM ; eluted with 0.25 M ; purity >99% by SDS-PAGE</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (unspecified)</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified FbpC (native and SeMet-labeled)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Not specified</td>
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
      <td>Crystals obtained for both native and SeMet-labeled FbpC. Data collected at ESRF beamline ID23eh1 (native, 1.9 A) and SRS 10.1 Daresbury (SeMet, 2.7 A). Structure solved by SeMet SAD phasing. Final Rwork/Rfree: 18.6%/23.4%.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### First domain-swapped NBD in ABC importers

FbpC is the first observation of [Three-Dimensional Domain Swapping](/xray-mp-wiki/concepts/structural-mechanisms/domain-swapping/) in ABC importers. The C-terminal regulatory domains undergo substantial swapping between the two monomers, forming a six-histidine cluster at the base of the dimer that may function as an  requisition store.

### Closed NBDs are tense

Molecular dynamics simulations of both FbpC and  showed that upon  removal, both NBDs open rapidly, demonstrating that the closed structures have higher free energies than their open states. This strain energy is built up when  binds and is released following hydrolysis, contributing to the power stroke of ABC transport.

### Electrostatic forces drive NBD opening

Both FbpC and  have significant areas of positive and negative charge distribution at the monomer interface. Electrostatic repulsion between the two NBD monomers is proposed as a major force driving the opening of the NBD dimer following  hydrolysis.

### Stochastic opening of ATP-binding interfaces

The opening of the two -binding interfaces within each NBD dimer appears to be stochastic and discrete, consistent with proposals that NBDs behave stochastically and that a single molecule of  may be sufficient to rearrange the TMDs and drive transport for some ABC transporters.


## Cross-References

- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — FbpC is the NBD of an ABC importer
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Used for induction of FbpC expression in E. coli
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Nickel-NTA</a> — Used in first affinity chromatography step for FbpC purification
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Used in second cobalt-affinity chromatography step
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Buffer used throughout FbpC purification
- <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> — Bound in the active site; used in purification buffers to stabilize FbpC
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Cryoprotectant in purification buffers
- <a href="/xray-mp-wiki/proteins/abc-transporters/malK/">Malk</a> — Referenced in fbpc text
- <a href="/xray-mp-wiki/reagents/additives/iron/">Iron</a> — Referenced in fbpc text
- <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a> — Referenced in fbpc text
