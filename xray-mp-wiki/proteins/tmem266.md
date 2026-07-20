---
title: "TMEM266 (mouse voltage-sensor protein)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1042##BCJ20220033]
verified: agent
uniprot_id: Q8BZB3
---

# TMEM266 (mouse voltage-sensor protein)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q8BZB3">UniProt: Q8BZB3</a>

<span class="expr-badge">Mus musculus</span>

## Overview

TMEM266 (C15orf27 in human) is a voltage-sensor domain (VSD)-containing protein primarily expressed in cerebellar granule cells of the mouse brain. Unlike the related Hv1/VSOP voltage-gated proton channel, TMEM266 does not exhibit ion channel activity but retains a functional voltage sensor that responds to rapid membrane potential changes on the microsecond timescale. The protein consists of an N-terminal voltage-sensor domain, a putative cytosolic coiled-coil region, and a C-terminal cytosolic region of unknown function. A short form splice variant (sTMEM266) lacking the C-terminal region was identified in mouse cerebellum. The crystal structure of the coiled-coil region (fTMEM266cc, residues 223-283) was determined at 2.30 A resolution (Kawai et al., 2022, PDB 7WJT), revealing a dimeric coiled-coil assembly with conserved heptad repeats, salt bridges (E258-R263, E276-R277), hydrogen bonds (Q269-D270), and a redox-dependent disulfide bond at C252. Proximity labeling (BioID) identified numerous TMEM266-interacting proteins involved in protein transport, folate homeostasis, and glucose metabolism. TMEM266-deficient mice showed reduced stereotypic counts in open-field tests, suggesting a role in regulating stereotyped behaviors.

## Publications

### doi/10.1042##BCJ20220033

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7wjt">7WJT</a></td>
      <td>2.30 A</td>
      <td>C2</td>
      <td>fTMEM266cc, coiled-coil region (residues 223-283) of mouse TMEM266, full-length form</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli BL21-CodonPlus(DE3)-RIPL
- **Construct**: fTMEM266cc (residues 223-283) with N-terminal MBP-His8-myc-His8 tag and TEV protease cleavage site, in pET-28b(+) vector

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
      <td>Affinity chromatography</td>
      <td>His-tag affinity (His8-myc-His8 tag)</td>
      <td>Not specified</td>
      <td>Not specified + --</td>
      <td>Protein expressed with N-terminal MBP-His8-myc-His8 tag. <a href="/xray-mp-wiki/reagents/enzymes/tev-protease/">TEV</a> protease cleavage site allowed tag removal after purification.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-drop vapor diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>fTMEM266cc (15 mg/ml) in buffer</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM MES-NaOH pH 6.0, 2% (v/v) 2-propanol, 200 mM calcium acetate</td>
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
      <td>Soaked in cryoprotective solution containing 100 mM MES-NaOH pH 6.0, 2% (v/v) 2-propanol, 200 mM calcium acetate, 30% (v/v) glycerol before flash freezing</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grown by sitting-drop vapor diffusion. Data collected at SPring-8 BL44XU beamline (Hyogo, Japan). Space group C2, cell dimensions a=60.3, b=90.5, c=49.2 A, beta=101.9 degrees. Resolution 37.91-2.30 A, 11376 unique reflections, 99.8% completeness, Rmerge=0.074, I/sigma=27.63 (4.50 in highest shell). Structure solved by molecular replacement using Hv1 coiled-coil (PDB 3A2A) as search model. Final Rwork/Rfree=0.225/0.257. Four chains (I-IV) identified in asymmetric unit. RMSD bonds 0.003 A, angles 0.600 degrees. MolProbity score 1.36, 98.66% favored, 0% outliers in Ramachandran plot.</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Dimeric coiled-coil structure

The crystal structure of the fTMEM266 coiled-coil region (residues 223-283, PDB 7WJT) reveals a parallel dimeric coiled-coil assembly at 2.30 A resolution. The heptad repeat pattern (abcdefg)n shows hydrophobic residues at the "a" and "d" positions, typical of coiled-coil structures. Two salt bridges (E258-R263 and E276-R277), a hydrogen-bond network (Q269-D270 and Q269-Q269), and a disulfide bond at C252 stabilize the dimer interface. The N-terminal half of the coiled-coil assembly has more open space than the corresponding Hv1/VSOP coiled-coil (PDB 3VMX), likely due to relatively hydrophilic residues at "a" and "d" positions in the upper half of the TMEM266 coiled-coil.

### Redox-dependent dimerization via C252

Cysteine 252 forms a disulfide bond in the crystal structure that mediates redox-dependent dimerization of TMEM266. Cross-linking experiments showed that the C252A mutant completely abolishes dimerization under both oxidizing (CuP) and reducing (DTT) conditions, while the Q269A mutant retains redox-dependent dimerization similar to wild-type. This suggests that C252 is essential for disulfide-mediated dimerization, similar to the redox-dependent regulation of Hv1/VSOP dimerization.

### Identification of short form TMEM266 (sTMEM266)

A novel short form splice variant of TMEM266 (sTMEM266) was identified in mouse cerebellum by 3-prime RACE. Alternative splicing at the donor site of exon 8 introduces a stop codon shortly after, resulting in a protein that retains the voltage-sensor domain and most of the coiled-coil region (with a different C-terminal sequence) but lacks the entire C-terminal cytosolic region. sTMEM266 forms homodimers but shows weak or no heterodimerization with fTMEM266 in cross-linking assays, suggesting preferential homodimer formation.

### Distinct interacting protein networks for fTMEM266 and sTMEM266

Proximity labeling (BioID) in Neuro-2A cells identified distinct sets of interacting proteins for fTMEM266 and sTMEM266. About 46% of interacting proteins were specific to fTMEM266, 23% were specific to sTMEM266, and 30% were shared. Shared proteins were mainly involved in protein transport (endocytosis, ubiquitin-proteasome, autophagy). fTMEM266-specific proteins included Rack1, Iqgap1, Rab5c, and Gnai2 (small GTPase-related signaling), while sTMEM266-specific proteins included RhoA and RanGAP1. This suggests the C-terminal region mediates distinct signaling pathway interactions.

### TMEM266 in cerebellar granule cell function

TMEM266 is predominantly expressed in cerebellar granule cells. TMEM266-deficient mice showed significantly reduced stereotypic counts in open-field tests but normal motor coordination (rota-rod, gait analysis), suggesting the protein is involved in regulating stereotyped behaviors rather than motor skill learning. The voltage sensor of TMEM266 can respond to rapid voltage changes on the microsecond timescale, indicating that neuronal action potentials may regulate TMEM266 activity in granule cells.

### Functional analogy with voltage-sensing phosphatases (VSP)

TMEM266 belongs to the family of unconventional voltage-sensor proteins that lack a pore-gate domain, similar to voltage-sensing phosphatases (VSP, which have phosphatase activity) and Hv1/VSOP (which forms a proton channel). Unlike Hv1/VSOP, TMEM266 shows no ion channel activity. Its C-terminal cytosolic region may mediate protein-protein interactions in a voltage-dependent manner, potentially functioning as a voltage-regulated scaffold or signaling module in cerebellar granule cells.


## Cross-References

- <a href="/xray-mp-wiki/concepts/construct-design/voltage-sensor-paddle/">Voltage-Sensor Paddle</a> — TMEM266 contains a canonical voltage-sensor domain homologous to Hv1/VSOP
- <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> — Buffer used in crystallization (100 mM MES-NaOH pH 6.0)
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Cryoprotectant used during crystal freezing (30% v/v)
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Used for purification of fTMEM266cc via His8-myc-His8 tag
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting-Drop Vapor Diffusion</a> — Method used for crystallization of fTMEM266cc
