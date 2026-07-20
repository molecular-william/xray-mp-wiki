---
title: "GluA2/3 Heteromeric AMPA Receptor"
created: 2026-06-11
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein, xray-crystallography]
sources: [doi/10.1126##science.aad3873]
verified: agent
uniprot_id: P19491
---

# GluA2/3 Heteromeric AMPA Receptor

<div class="expr-badges"><span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P19491">UniProt: P19491</a>

<span class="expr-badge">Rattus norvegicus</span>

## Overview

GluA2/3 is a heteromeric AMPA-type ionotropic glutamate receptor composed of GluA2 and GluA3 subunits, representing the predominant form of AMPA receptors in the brain. The crystal structure of the GluA2/3 N-terminal domain (NTD) heteromer was determined at 2.1 A resolution, revealing a novel compact 'O-shape' tetrameric arrangement with alternating subunits around a central axis, in contrast to the 'N-shape' arrangement of GluA2 homomers. [Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) structures of the full-length GluA2/3 heteromer at 8.25 A and 10.3 A resolution captured the receptor in resting and desensitized states, revealing substantial vertical compression and close NTD-LBD associations resembling NMDA receptors. GluA2 occupies the pore-proximal (AC) position while GluA3 occupies the pore-distal (BD) position. The work reveals organizational features of heteromeric AMPARs and provides snapshots of gating transitions.


## Publications

### doi/10.1126##science.aad3873

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5fwx">5FWX</a></td>
      <td>2.1</td>
      <td></td>
      <td>GluA2/3 NTD heteromer (GluA2 residues 1-379, GluA3 residues 1-380)</td>
      <td>none</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5fwx">5FWX</a></td>
      <td>2.5</td>
      <td></td>
      <td>GluA2/4 NTD heteromer</td>
      <td>none</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnTI- cells (stable transfection)
- **Construct**: GluA2 NTD (residues 1-379), GluA3 NTD (residues 1-380), GluA4 NTD (residues 1-380)

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
      <td>Expression</td>
      <td>Stable transfection in HEK293S GnTI- cells</td>
      <td>—</td>
      <td>DMEM culture medium</td>
      <td>Proteins produced in stably transfected HEK293S-GnTI- cells</td>
    </tr>
    <tr>
      <td>Initial purification</td>
      <td>Cross-flow concentration and dialysis</td>
      <td>—</td>
      <td>1 M NaCl, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8</td>
      <td>Cross-flow concentration followed by dialysis</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td>HisTrap HP column</td>
      <td>HisTrap HP (GE Healthcare)</td>
      <td>1 M NaCl, 50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> pH 8 + not specified</td>
      <td></td>
    </tr>
    <tr>
      <td>Size exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a> - S200 (GE Healthcare)</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.4, 150 mM NaCl</td>
      <td><a href="/xray-mp-wiki/reagents/additives/endoh/">Endoh</a> treatment for deglycosylation in 100 mM sodium <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a> pH 5.2, followed by final <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
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
      <td>GluA2/3 NTD heteromer at 22 mg/ml (mixed stepwise from GluA3 5 mg/ml + GluA2 0.5 mg/ml)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>14-16% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 3350, 0.27 M ammonium sulfate, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/bicine/">Bicine</a> pH 9</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>GluA2/3 NTD crystallized at 12.5 mg/ml. GluA2/4 NTD crystallized in 17% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 3350, 0.1-0.35 M ammonium sulfate. Data collected at Diamond Light Source I04-1 beamline.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### O-shape NTD tetramer with alternating subunit arrangement

The GluA2/3 and GluA2/4 NTD heterodimers assemble into a novel tetrameric arrangement called the O-shape, where the four subunits alternate around a central axis. This is distinct from the N-shape seen in GluA2 homomers. The tetrameric interface harbors three major contact regions mediated predominantly by the upper lobes (ULs), with GluA2 at specific diagonal positions. The arrangement is reminiscent of NMDA receptors.

### Vertical compression of the extracellular region

The GluA2/3 heteromer exhibits substantial vertical compression compared to GluA2 homomers. The center of mass distance between the NTD layer and the gate residue Thr625 is 76 A in GluA2/3 (M1), compared to 97 A in GluA2 homomers. This compression is akin to NMDAR architecture and brings the NTD and LBD layers into close contact, creating novel inter-layer interfaces.

### Two distinct ligand-free states captured by cryo-EM

[Cryo Em](/xray-mp-wiki/methods/structure-determination/cryo-em/) revealed two models of GluA2/3 in the nominal absence of ligand. Model 1 (M1, 8.25 A) resembles a resting state with intact LBD dimers. Model 2 (M2, 10.3 A) resembles a desensitized state with one LBD dimer ruptured. These provide snapshots of gating transitions in the apo state.

### Subunit positioning in heteromeric AMPARs

In the GluA2/3 heteromer, GluA2 occupies the pore-proximal (AC) position and GluA3 occupies the pore-distal (BD) position at the LBD and TMD levels. However, subunit placement does not follow strict rules, as GluA2 can also occupy the BD position according to the crystal lattice, contrasting with obligatory iGluR heteromers like NMDARs.

### NTD compaction is compatible with gating

Crosslinking the NTD layer in the O-shape conformation did not impair receptor function. O-crosslinked mutants showed similar peak currents, desensitization kinetics, and recovery from desensitization compared to wild-type. This demonstrates that rupture of the NTD layer is not a prerequisite for desensitization, and a compact NTD arrangement permits LBD dynamics and gating transitions.


## Cross-References

- <a href="/xray-mp-wiki/proteins/other-ion-channels/glua2-ampa-receptor/">GluA2 AMPA Receptor</a> — GluA2 is a subunit of the GluA2/3 heteromeric AMPA receptor
- <a href="/xray-mp-wiki/concepts/signaling-receptors/desensitization-in-cys-loop-receptors/">Desensitization in Cys-loop Receptors</a> — The M1/M2 states reveal desensitization-like transitions in AMPARs
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em/">Cryo Em</a> — Referenced in glua2-3-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Referenced in glua2-3-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> — Referenced in glua2-3-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/buffers/acetate/">Acetate</a> — Referenced in glua2-3-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/additives/endoh/">Endoh</a> — Referenced in glua2-3-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/buffers/bicine/">Bicine</a> — Referenced in glua2-3-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> — Referenced in glua2-3-ampa-receptor text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in glua2-3-ampa-receptor text
