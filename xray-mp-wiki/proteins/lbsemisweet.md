---
title: "LbSemiSWEET from Leptospira biflexa"
created: 2026-05-27
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.cell.2017.03.010, doi/10.1038##nature13670]
verified: agent
uniprot_id: B0SR19
---

# LbSemiSWEET from Leptospira biflexa

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/B0SR19">UniProt: B0SR19</a>

<span class="expr-badge">Leptospira biflexa serovar patoc (strain patoc 1 / ATCC 23582 / paris)</span>

## Overview

LbSemiSWEET is a sugar transporter from the SWEET family found in the bacterium Leptospira biflexa. It is among the smallest characterized transporters at less than 20 kDa, with a simple geometry as a symmetric dimer of three-helix bundles. LbSemiSWEET transports a single substrate ([Glucose](/xray-mp-wiki/reagents/additives/glucose/)) and operates via an alternating-access mechanism. The SWEET family is widespread and plays critical roles in phloem loading, nectar secretion, pollen development, and seed filling in plants.


## Publications

### doi/10.1016##j.cell.2017.03.010

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uhs">5UHS</a></td>
      <td>2.8</td>
      <td>P212121</td>
      <td>LbSemiSWEET D57A mutant</td>
      <td><a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5uhq">5UHQ</a></td>
      <td>2.8</td>
      <td>P212121</td>
      <td>LbSemiSWEET Q20A mutant</td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: LbSemiSWEET with C-terminal 3C protease recognition site and 10xHis-tag
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/), 22 C overnight

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
      <td>TBS (50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl)</td>
      <td>Pelleted cells resuspended in TBS and lysed by sonication</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>TBS with 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (2% w/v)</td>
      <td>Solubilized for 2 hours at 4 C; insoluble debris pelleted at 16,000 rpm</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Cobalt <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>HisPur cobalt resin</td>
      <td>TBS with 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (0.1%)</td>
      <td>His-tag cleaved by 3C protease to elute protein</td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>10 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.0, 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (0.03%)</td>
      <td>Peak fractions pooled, concentrated, flash frozen in liquid N2, stored at -80 C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>LbSemiSWEET D57A reconstituted with <a href="/xray-mp-wiki/reagents/lipids/monovaccenin/">Monovaccenin</a> (1:1.5 wt/wt)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew within one week; D57A mutation favors outward-open conformation</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/vapor-diffusion/">Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>LbSemiSWEET Q20A reconstituted with <a href="/xray-mp-wiki/reagents/lipids/monopalmitolein/">Monopalmitolein</a> (1:1.5 wt/wt)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals appeared within two days; Q20A mutation favors inward-open conformation</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5uhs">5UHS</a> — Chain A (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">MENL</span><span class="topo-membrane">IGYVAAFLTTVSFLPQVLRVV</span><span class="topo-outside">MTKQTRDI</span><span class="topo-membrane">SRNMYIMFFLGVVLWFVYGI</span><span class="topo-inside">LRSAL</span><span class="topo-membrane">PIILANVVTLFFVTIILYYKLT</span><span class="topo-outside">E</span><span class="topo-unknown">GNQTGSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>5</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>33</td>
      <td>26</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>34</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>58</td>
      <td>54</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>80</td>
      <td>59</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5uhs">5UHS</a> — Chain B (3 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">MENL</span><span class="topo-membrane">IGYVAAFLTTVSFLPQVLRVV</span><span class="topo-outside">MTKQTRDI</span><span class="topo-membrane">SRNMYIMFFLGVVLWFVYGI</span><span class="topo-inside">LRSAL</span><span class="topo-membrane">PIILANVVTLFFVTIILYYKL</span><span class="topo-outside">TE</span><span class="topo-unknown">GNQTGSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (7 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>25</td>
      <td>5</td>
      <td>25</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>26</td>
      <td>33</td>
      <td>26</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>53</td>
      <td>34</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>58</td>
      <td>54</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>79</td>
      <td>59</td>
      <td>79</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>80</td>
      <td>81</td>
      <td>80</td>
      <td>81</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5uhq">5UHQ</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90   </span>
<span class="topo-line"><span class="topo-inside">MENLIGYVAAFLTTVSFLPAVLRVVMTKQTRD</span><span class="topo-membrane">ISRNMYIMFFLGVVLWFVYGIL</span><span class="topo-outside">RSDL</span><span class="topo-membrane">PIILANVVTLFFVTIILYYKLTE</span><span class="topo-inside">GNQTGSLEVLFQ</span></span>
<details class="topo-details"><summary>Topology coordinates (5 regions)</summary>
<table class="wiki-mini-table">
  <thead><tr>
    <th>Begin</th>
    <th>End</th>
    <th>PDB Begin</th>
    <th>PDB End</th>
    <th>Location</th>
  </tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>32</td>
      <td>1</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>54</td>
      <td>33</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>58</td>
      <td>55</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>59</td>
      <td>81</td>
      <td>59</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>82</td>
      <td>93</td>
      <td>82</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature13670

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4qnc">4QNC</a></td>
      <td>2.40</td>
      <td>P21</td>
      <td>Full-length L. biflexa serovar Patoc <a href="/xray-mp-wiki/concepts/transport-mechanisms/semisweet/">SemiSWEET Transporter Family</a></td>
      <td>--</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli
- **Construct**: LbSemiSWEET with C-terminal 3C protease recognition site and 10xHis-tag
- **Induction**: 0.2 mM [IPTG](/xray-mp-wiki/reagents/additives/iptg/), 22 C overnight

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>L. biflexa serovar Patoc <a href="/xray-mp-wiki/concepts/transport-mechanisms/semisweet/">SemiSWEET Transporter Family</a> reconstituted into <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> (1:1.5 protein:lipid)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals grew in about 1 week; captured in occluded conformation</td>
    </tr>
  </tbody>
</table>

## Biological / Functional Insights

### Alternating-access transport mechanism

LbSemiSWEET undergoes spontaneous transitions between outward-open, occluded, and inward-open conformations. The extracellular gate (Tyr51, Ile60, Arg55, Asp57) closes first, followed by opening of the intracellular gate (Phe17, Met37, Tyr38, Phe41). The occluded state is an on-pathway intermediate that acts as an air lock, preventing simultaneous opening of both gates.

### Glucose translocation as a free ride

MD simulations reveal that [Glucose](/xray-mp-wiki/reagents/additives/glucose/) takes a free ride across the membrane, with the transporter adopting the same conformational transitions with and without substrate. The apparent Km for [Glucose](/xray-mp-wiki/reagents/additives/glucose/) is ~70 uM for D57A mutant and ~160 uM for wild-type. [Glucose](/xray-mp-wiki/reagents/additives/glucose/) binds off-center between Trp48 residues on each protomer, coordinated by Asn64 and Thr13 on one protomer.

### Gating residue mutagenesis

Alanine substitution of extracellular gate residues Tyr51, Ile60, and intracellular gate residues Phe17, Met37, and Tyr38 ablated [Glucose](/xray-mp-wiki/reagents/additives/glucose/) uptake. Asp57, Arg55, Met37, and Phe41 mutations had no significant effect on activity. The D57A mutation increased [Glucose](/xray-mp-wiki/reagents/additives/glucose/) affinity more than two-fold compared to wild-type.

### Occluded state structure

The L. biflexa [SemiSWEET Transporter Family](/xray-mp-wiki/concepts/transport-mechanisms/semisweet/) structure at 2.40 Å resolution captures an occluded conformation. At the extracellular side, D57 from one protomer forms hydrogen bonds with Y51 from the other protomer, shielding the cavity from the extracellular solution. A strong non-protein electron density is present at the cavity center, surrounded by W48 and N64 from both protomers. The antiparallel aromatic ring of tryptophan from each protomer is within 4 Å of the putative substrate. W48 and N64 are implicated as critical residues in substrate binding and translocation.


## Cross-References

- <a href="/xray-mp-wiki/proteins/miscellaneous/vibrio-sp-semisweet/">Vibrio sp. SemiSWEET</a> — Related bacterial SemiSWEET crystallized in outward-open state at 1.70 Å
- <a href="/xray-mp-wiki/proteins/miscellaneous/a-thaliana-sweet1/">A. thaliana SWEET1</a> — Plant SWEET1 with conserved W and N residues critical for sugar transport
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — LbSemiSWEET operates via alternating access with spontaneous conformational transitions
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/sweet-transporter/">SWEET Transporter Family</a> — LbSemiSWEET is a member of the SWEET family of sugar transporters
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> — Primary detergent used for solubilization and purification
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Substrate transported by LbSemiSWEET; used in crystallization
- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Lipid used in lipidic cubic phase crystallization
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/semisweet/">SemiSWEET Transporter Family</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/concepts/alternating-access/">Alternating Access Mechanism</a> — LbSemiSWEET exemplifies the alternating access model of transporter function
- <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic Cubic Phase (LCP) Crystallization</a> — Both D57A and Q20A mutants were crystallized using LCP with monoacylglycerols
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-dynamics-simulation/">Molecular Dynamics Simulation</a> — MD simulations captured spontaneous outward-open to inward-open transitions
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris (Tris-HCl Buffer)</a> — Tris-HCl pH 8.0 used as main purification buffer and crystallization reservoir
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG 400 (Polyethylene Glycol 400)</a> — Used as precipitant in both D57A and Q20A crystallization conditions
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/miscellaneous/lbsemisweet/">LbSemiSWEET from Leptospira biflexa</a> — Related protein structure
