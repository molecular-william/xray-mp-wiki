---
title: "BcTSPO Translocator Protein from Bacillus cereus"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein]
sources: [doi/10.1126##science.aaa1534]
verified: agent
uniprot_id: Q81BL7
---

# BcTSPO Translocator Protein from Bacillus cereus

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q81BL7">UniProt: Q81BL7</a>

<span class="expr-badge">Bacillus cereus</span>

## Overview

BcTSPO is the translocator protein (TSPO) homolog from *Bacillus cereus*, a bacterial member of the tryptophan-rich TSPO family. Crystal structures were determined for the apo form at 1.7 Å resolution and for the PK11195-bound dimer, revealing a five-transmembrane-helix fold with a highly conserved ligand-binding pocket between TM1 and TM2. BcTSPO binds the benzodiazepine ligand [Pk11195](/xray-mp-wiki/reagents/ligands/pk11195/) and the endogenous porphyrin protoporphyrin IX (PpIX), and catalyzes the photooxidative degradation of PpIX — a reaction involving conserved tryptophan residues W51 and W138. The A142T mutation (corresponding to the human A147T polymorphism associated with psychiatric disorders) abrogates PpIX degradation activity and alters ligand binding.


## Publications

### doi/10.1126##science.aaa1534

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ryq">4RYQ</a></td>
      <td>1.7</td>
      <td>—</td>
      <td>Wild-type BcTSPO (apo)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4ryq">4RYQ</a></td>
      <td>—</td>
      <td>—</td>
      <td>PK11195-bound BcTSPO dimer</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Wild-type BcTSPO and variants (W51F, W138F, W51F/W138F, A142T)

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
      <td>Protein purification</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity chromatography</a></td>
      <td>—</td>
      <td></td>
      <td>Purified BcTSPO used for crystallization and activity assays</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>) and detergent micelle</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Apo structure solved from detergent micelle at 1.7 Å. PK11195-bound dimer crystallized in <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>. Apo micelle may be a swapped dimer.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ryq">4RYQ</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKHHHHHHHHHHENLYFQSYVMF</span><span class="topo-outside">MKKS</span><span class="topo-membrane">SIIVFFLTYGLFYVSSVLFP</span><span class="topo-inside">ID</span><span class="topo-unknown">RTWYDA</span><span class="topo-inside">LEKPSWTPPGM</span><span class="topo-membrane">TIGMIWAVLFGLIALSVAIIY</span><span class="topo-outside">NNYGFKPK</span><span class="topo-membrane">TFWFLFLLNYIFNQAFSY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180 </span>
<span class="topo-line"><span class="topo-membrane">FQ</span><span class="topo-inside">FSQKNLF</span><span class="topo-membrane">LATVDCLLVAITTLLLIMFSS</span><span class="topo-outside">NLSK</span><span class="topo-membrane">VSAWLLIPYFLWSAFATYLSW</span><span class="topo-inside">TIYSIN</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>31</td>
      <td>34</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>54</td>
      <td>7</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>56</td>
      <td>27</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>62</td>
      <td>29</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>73</td>
      <td>35</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>94</td>
      <td>46</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>102</td>
      <td>67</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>122</td>
      <td>75</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>129</td>
      <td>95</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>150</td>
      <td>102</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>154</td>
      <td>123</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>175</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>181</td>
      <td>148</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4ryq">4RYQ</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MDYKDDDDKHHHHHHHHHHENLYFQSYVMF</span><span class="topo-outside">MKKS</span><span class="topo-membrane">SIIVFFLTYGLFYVSSVLFP</span><span class="topo-inside">ID</span><span class="topo-unknown">RTWYDA</span><span class="topo-inside">LEKPSWTPPGM</span><span class="topo-membrane">TIGMIWAVLFGLIALSVAIIY</span><span class="topo-outside">NNYGFKPK</span><span class="topo-membrane">TFWFLFLLNYIFNQAFSY</span></span>
<span class="topo-ruler">       130       140       150       160       170       180 </span>
<span class="topo-line"><span class="topo-membrane">FQ</span><span class="topo-inside">FSQKNLF</span><span class="topo-membrane">LATVDCLLVAITTLLLIMFSS</span><span class="topo-outside">NLSK</span><span class="topo-membrane">VSAWLLIPYFLWSAFATYLSW</span><span class="topo-inside">TIYSIN</span></span>
<details class="topo-details"><summary>Topology coordinates (13 regions)</summary>
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
      <td>31</td>
      <td>34</td>
      <td>3</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>54</td>
      <td>7</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>56</td>
      <td>27</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>57</td>
      <td>62</td>
      <td>29</td>
      <td>34</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>63</td>
      <td>73</td>
      <td>35</td>
      <td>45</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>94</td>
      <td>46</td>
      <td>66</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>95</td>
      <td>102</td>
      <td>67</td>
      <td>74</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>122</td>
      <td>75</td>
      <td>94</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>123</td>
      <td>129</td>
      <td>95</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>130</td>
      <td>150</td>
      <td>102</td>
      <td>122</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>151</td>
      <td>154</td>
      <td>123</td>
      <td>126</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>155</td>
      <td>175</td>
      <td>127</td>
      <td>147</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>176</td>
      <td>181</td>
      <td>148</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Conserved five-helix TSPO fold

BcTSPO adopts a five-transmembrane-helix bundle (TM1–TM5). The protein is tryptophan-rich, with four conserved tryptophans (W31, W40, W51, W138) that play key roles in structure and function. The fold is distinct from the NMR model of mouse TSPO1 (MmTSPO1, PDB 2MGY) but closely matches the [Rstspo](/xray-mp-wiki/proteins/structural-adhesion/rstspo/) structure from R. sphaeroides (PDB 4UC1).

### PK11195 binding pocket

[Pk11195](/xray-mp-wiki/reagents/ligands/pk11195/) binds in a highly conserved cavity between TM1 and TM2. The ligand's carbonyl oxygen forms hydrogen bonds with the indole-NH groups of W51 and W138. The chloride atom contacts N87. Additional van der Waals contacts involve residues from all five helices and the TM1–TM2 loop. The binding pocket is water-filled in the apo structure, and protoporphyrin IX can be docked into the same cavity.

### Photooxidative degradation of protoporphyrin IX

BcTSPO catalyzes the light-dependent degradation of protoporphyrin IX (PpIX), involving oxidative cleavage at the methene bridge between vinyl-bearing pyrrole rings. Conserved tryptophans W51 and W138 are poised near the scissile methene bridge and vinyl groups. The W51F/W138F double mutant and the A142T mutant both lose PpIX degradation activity. The degradation product has spectral features reminiscent of biliverdin and phycocyanobilin, suggesting a formyl analog of biliverdin as a plausible product. [Pk11195](/xray-mp-wiki/reagents/ligands/pk11195/) binding substantially inhibits PpIX decay.

### A142T mutation mimics human A147T polymorphism

The A142T mutation in BcTSPO corresponds to the human A147T polymorphism associated with psychiatric disorders and reduced pregnenolone production. Ala142 projects into the binding pocket; mutation to threonine interferes with ligand binding. The A142T mutation abrogates PpIX photooxidative activity and is consistent with the reduced binding affinity for PET radioligands PBR28 and [18F]-FEPPA observed in human A147T carriers.


## Cross-References

- <a href="/xray-mp-wiki/reagents/ligands/pk11195/">PK11195</a> — PK11195 is a high-affinity ligand of BcTSPO, binding in the conserved pocket between TM1 and TM2
- <a href="/xray-mp-wiki/reagents/ligands/protoporphyrin-ix/">Protoporphyrin IX (PpIX)</a> — PpIX is an endogenous porphyrin ligand that is photooxidatively degraded by BcTSPO
- <a href="/xray-mp-wiki/proteins/structural-adhesion/rstspo/">RsTSPO Translocator Protein from Rhodobacter sphaeroides</a> — BcTSPO and RsTSPO share the conserved five-helix TSPO fold and are bacterial homologs of mammalian TSPO
