---
title: "NmEptA - Lipid A Phosphoethanolamine Transferase from Neisseria meningitidis"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein]
sources: [doi/10.1073##pnas.1612927114]
verified: regex
uniprot_id: Q7DD94
---

# NmEptA - Lipid A Phosphoethanolamine Transferase from Neisseria meningitidis

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q7DD94">UniProt: Q7DD94</a>

<span class="expr-badge">Neisseria meningitidis serogroup B</span>

## Overview

NmEptA is a [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) phosphoethanolamine (PEA) transferase from *Neisseria meningitidis* that catalyzes the transfer of phosphoethanolamine from [Phosphatidylethanolamine](/xray-mp-wiki/reagents/lipids/phosphatidylethanolamine/) to the 1 and 4' headgroup positions of [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/). This modification masks the negatively charged phosphate groups on the bacterial surface, conferring resistance to cationic antimicrobial peptides (CAMPs) such as colistin. The full-length X-ray crystal structure at 2.75 Å resolution reveals a helical transmembrane domain and a periplasmic-facing soluble hydrolase-fold domain connected by a bridging helix. A Zn2+ ion is tetrahedrally coordinated at the active site, with Thr280 serving as the catalytic nucleophile. The structure provides insights into conformational dynamics that enable binding of two differently-sized lipid substrates and informs structure-guided drug design for treating multidrug-resistant bacterial infections.

## Publications

### doi/10.1073##pnas.1612927114

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5fgn">5FGN</a></td>
      <td>2.75</td>
      <td>—</td>
      <td>Full-length NmEptA (hexahistidine-tagged)</td>
      <td>Zn2+, <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli
- **Construct**: Full-length NmEptA with N-terminal hexahistidine tag

**Purification:**

- **Expression system**: E. coli
- **Expression construct**: Full-length NmEptA with hexahistidine tag

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
      <td>Solubilization</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Enzyme expressed recombinantly and purified in presence of <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni2+-NTA</td>
      <td>Ni-NTA</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td>SEC</td>
      <td>Not specified</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td></td>
    </tr>
  </tbody>
</table>
**Final sample**: Purified NmEptA in [DDM](/xray-mp-wiki/reagents/detergents/ddm/) micelles
**Purity**: Monodisperse and thermally stable

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Not specified in main text</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified full-length NmEptA in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Structure solved by <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> using soluble domain structure (PDB 4KAV). Data collected at Diamond Light Source and Australian Synchrotron.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5fgn">5FGN</a> — Chain A (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MIKPNLR</span><span class="topo-inside">PKLG</span><span class="topo-membrane">SSALIAFLSLYSSLVLNY</span><span class="topo-outside">AFFAKVVELHPFNGTGADIFLY</span><span class="topo-membrane">TMPVVLFFLSNFVFHVIALPF</span><span class="topo-inside">V</span><span class="topo-membrane">HKVLIPLILVISAAVSY</span><span class="topo-outside">QEIFFNIYFN</span><span class="topo-unknown">KSMLNNVLQ</span><span class="topo-outside">TTAAESARLIT</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">P</span><span class="topo-membrane">GYVLWIVCLGVLPALAYIAV</span><span class="topo-inside">KVKYRVWYKEFL</span><span class="topo-membrane">TRLVLAAVSFLCALGIAML</span><span class="topo-outside">Q</span><span class="topo-unknown">YQDYASFFRN</span><span class="topo-outside">NKSVTHLIVPSNFI</span><span class="topo-unknown">GAGVSKYKDWKRSNI</span><span class="topo-outside">PYTQLDMAVVQNRPAGSLRRFVVLVVGE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TTRAANWGLNGYSRQTTPLLAARGDEIVNFPQVRSCGTSTAHSLPCMFSTFDRTDYDEIKAEHQDNLLDIVQRAGVEVTWLENDSGCKGVCGKVPNTDVTSLNLPEYCRNGECLDNILLT</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">KFDEVLNKNDKDAVLILHTIGSHGPTYYERYTEAERKFTPTCDTNEINKCTRATLVNTYDNTVLYVDQFIDKVIRKLENRDDLESVVHYVSDHGESLGENGMYLHAAPYAIAPSGQTHIP</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550</span>
<span class="topo-line"><span class="topo-outside">MVMWFSKAFRQHGGIDFQCLKQKAAENEYSHDHYFSTVLGLMDISNSQTYRKEMDILAACRRP</span><span class="topo-unknown">RHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (17 regions)</summary>
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
      <td>8</td>
      <td>11</td>
      <td>8</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>29</td>
      <td>12</td>
      <td>29</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>30</td>
      <td>51</td>
      <td>30</td>
      <td>51</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>72</td>
      <td>52</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>73</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>90</td>
      <td>74</td>
      <td>90</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>91</td>
      <td>100</td>
      <td>91</td>
      <td>100</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>101</td>
      <td>109</td>
      <td>101</td>
      <td>109</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>110</td>
      <td>121</td>
      <td>110</td>
      <td>121</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>141</td>
      <td>122</td>
      <td>141</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>153</td>
      <td>142</td>
      <td>153</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>154</td>
      <td>172</td>
      <td>154</td>
      <td>172</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>173</td>
      <td>173</td>
      <td>173</td>
      <td>173</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>174</td>
      <td>183</td>
      <td>174</td>
      <td>183</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>184</td>
      <td>197</td>
      <td>184</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>198</td>
      <td>212</td>
      <td>198</td>
      <td>212</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>213</td>
      <td>543</td>
      <td>213</td>
      <td>543</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Full-length structure reveals membrane domain architecture

The 2.75 Å crystal structure of full-length NmEptA reveals a previously uncharacterized helical membrane domain comprising five transmembrane helices (TMH1-5), two periplasmic-facing helices (PH1-PH2 and PH2'), and a bridging helix that connects to the soluble domain. The soluble domain adopts a hydrolase-type fold with a bound Zn2+ ion at the active site. A large interdomain interface (~1,200 Å2) with high sequence conservation suggests functional coupling between domains.

### Substrate binding by PH2 and PH2' helices

Two amphipathic helices located in a periplasmic loop between TMH3 and TMH4 (PH2 and PH2') contain conserved charged residues implicated in lipid substrate binding. A bound [DDM](/xray-mp-wiki/reagents/detergents/ddm/) molecule was observed in the active site between these helices, with the carbohydrate moiety forming hydrogen bonds with three invariant residues. The O3B hydroxyl of [DDM](/xray-mp-wiki/reagents/detergents/ddm/) is positioned 3.72 Å from the bound Zn2+ and 2.96 Å from the catalytic Thr280.

### Conformational dynamics enable dual substrate recognition

[Limited Proteolysis](/xray-mp-wiki/methods/purification/limited-proteolysis/), intrinsic tryptophan fluorescence, and molecular dynamics simulations suggest NmEptA samples different conformational states. In [DDM](/xray-mp-wiki/reagents/detergents/ddm/) and [Cymal-6](/xray-mp-wiki/reagents/detergents/cymal-6/), the enzyme adopts a conformation conducive to PEA hydrolysis, while in Fos-choline-12 it adopts a non-productive state. MD simulations show the soluble domain can dissociate from the membrane domain and "roll" over the membrane surface, suggesting a range of conformations for binding two differently-sized lipid substrates (PE and [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/)).

### Comparison with ArnT

[ARNT](/xray-mp-wiki/proteins/enzymes/arnt/) is a related lipid-to-lipid glycosyltransferase that modifies the same sites on [Lipid A](/xray-mp-wiki/reagents/lipids/lipid-a/) with 4-amino-4-deoxy-L-arabinose. While both enzymes are located in the periplasmic membrane with TM and soluble domains, [ARNT](/xray-mp-wiki/proteins/enzymes/arnt/) has 13 TM helices and a smaller soluble domain. NmEptA employs a ping-pong mechanism via a Thr280-PEA intermediate, whereas [ARNT](/xray-mp-wiki/proteins/enzymes/arnt/) requires both substrates to bind simultaneously for direct transfer.


## Cross-References

- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltoside (DDM)</a> — Primary detergent used for solubilization, purification, and crystallization of NmEptA
- <a href="/xray-mp-wiki/reagents/detergents/cymal-6/">Cymal-6</a> — Alternative maltoside detergent used in conformational studies
- <a href="/xray-mp-wiki/reagents/detergents/foscholine-12/">Foscholine-12</a> — Zwitterionic detergent used in conformational studies showing non-productive state
- <a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6-tag</a> — Affinity tag used for purification
- <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Nickel-NTA</a> — Affinity resin for purification of hexahistidine-tagged NmEptA
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/limited-proteolysis/">Limited Proteolysis</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/enzymes/arnt/">ARNT</a> — Related protein structure
