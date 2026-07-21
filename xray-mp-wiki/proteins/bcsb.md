---
title: "BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit)"
created: 2026-06-03
updated: 2026-07-20
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature11744]
verified: agent
uniprot_id: ['Q3J125', 'Q3J126']
---

# BcsB from Rhodobacter sphaeroides (Cellulose Synthase Periplasmic Subunit)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q3J125">UniProt: Q3J125</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q3J126">UniProt: Q3J126</a>

<span class="expr-badge">Rhodobacter sphaeroides</span>

## Overview

BcsB is a periplasmic protein that associates with the catalytic [Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) subunit to form the bacterial cellulose synthase complex from Rhodobacter sphaeroides. BcsB is anchored to the inner membrane via a single C-terminal transmembrane helix and contains two periplasmic carbohydrate binding domains (CBD1 and CBD2) connected by a conserved disulphide bond, and two flavodoxin-like domains (FD1 and FD2). The CBD domains interact with the translocating glucan chain as it exits the [Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) transmembrane channel, while the conserved residues at the tip of CBD1 likely play a role in glucan binding. [Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) and BcsB can be fused as a single polypeptide in some species, supporting the genetic observation that BcsB is essential for cellulose synthesis.

## Publications

### doi/10.1038##nature11744

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4hg6">4HG6</a></td>
      <td>4.5 A</td>
      <td></td>
      <td>BcsA-BcsB complex from Rhodobacter sphaeroides; BcsB residues 21-725 with N-terminal PelB signal sequence (generates additional Met-Gly dipeptide after cleavage)</td>
      <td>Translocating glucan (18 <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> units visible in electron density)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli Rosetta 2 cells
- **Construct**: BcsB residues 21-725 cloned into pETDuet vector with N-terminal PelB signal sequence; amplified without native N-terminal signal sequence

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
      <td>Co-expression and membrane preparation</td>
      <td>Auto-induction culture</td>
      <td>--</td>
      <td>ZYP-5052 auto-induction medium + --</td>
      <td><a href="/xray-mp-wiki/proteins/enzymes/bcsa/">Bcsa</a> and BcsB co-expressed in E. coli Rosetta 2 cells; cells grown at 37 C in ZYP-5052 auto-induction medium</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM sodium phosphate pH 7.2, 0.3 M NaCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/cellobiose/">Cellobiose</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a>, 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 2% Triton X-100</td>
      <td>Crude membranes solubilized for 60 min at 4 C</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose (Qiagen)</td>
      <td>RB2 buffer with 40 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> + 2% Triton X-100</td>
      <td>Batch incubation with <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose; <a href="/xray-mp-wiki/proteins/enzymes/bcsa/">Bcsa</a> carries C-terminal His12 tag for purification of the complex</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified BcsA-BcsB complex</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>30% <a href="/xray-mp-wiki/reagents/additives/peg200/">PEG200</a>, 0.1 M <a href="/xray-mp-wiki/reagents/buffers/mes/">MES</a> pH 6.5, 50 mM NaCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>approximately 7 days for initial crystals</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals of selenomethionine-derivatized BcsA-BcsB complex grown at 4 C; diffraction to 4.5 A</td>
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
      <td>6.5</td>
    </tr>
    <tr>
      <td>Temperature (structured)</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Components</td>
      <td>- Peg: 30 % [precipitant] (PEG200)  
- Mes: 0.1 M [buffer]  
- Sodium Chloride: 50 mM [salt]</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hg6">4HG6</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MTVRAKARSPLRV</span><span class="topo-membrane">VPVLLFLLWVALLVPFGLLAA</span><span class="topo-outside">APVAPSAQ</span><span class="topo-membrane">GLIALSAVVLVALLKPFA</span><span class="topo-inside">DKM</span><span class="topo-membrane">VPRFLLLSAASMLVMRYWFWRLF</span><span class="topo-outside">ETLPPPAL</span><span class="topo-membrane">DASFLFALLLFAVETFSISIFFLNGF</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LSADPTDRPFPRPLQPEELPTVDILVPSYNEPADMLSVTLAAAKNMIYPARLRTVVLCDDGGTDQRCMSPDPELAQKAQERRRELQQLCRELGVVYSTRERNEHAKAGNMSAALERLKGE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">LVVVFDADHVPSRDFLARTVGYFVEDPDLFLVQTPHFFINPDPIQRNLALGDRCPPENEMFYGKIHRGLDRWGGAFFCGSAAVLRRRALDEAGGFAGETITEDAETALEIHSRGWKSLYI</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">DRAMIAGLQPETFASFIQQRGRWATGMMQMLLLKNPLFRRGLGIAQRLCYLNSMSFWF</span><span class="topo-membrane">FPLVRMMFLVAPLIYLFFGIE</span><span class="topo-outside">IFVATFEEV</span><span class="topo-membrane">LAYMPGYLAVSFLVQNA</span><span class="topo-inside">LFARQRWPLVSEVYE</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VAQAPYLARAIVTTLLRPRSARFAVTAKDETLSENYISPIYRPLL</span><span class="topo-membrane">FTFLLCLSGVLATLVRWV</span><span class="topo-outside">AFPGDRSV</span><span class="topo-membrane">LLVVGGWAVLNVLLVG</span><span class="topo-inside">FALRAVAEKQQRRAAPRVQMEVPAEAQIPAFGN</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">RSLTATVLDASTSGVRLLVRLPGVGDPHPALEAGGLIQFQPKFPDAPQLERMVRGRIRSARREGGTVMVGVIFEAGQPIAVRETVAYLIFGESAHWRTMREATMRPIGLLHGMARILWMA</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800  </span>
<span class="topo-line"><span class="topo-inside">AASLPKTARDFMDEPARRRRRHEEPKEKQAHLLAFGTDF</span><span class="topo-unknown">STEPDWAGELLDPTAQVSARPNTVAWGSNHHHHHHKLHHHHHH</span></span>
<details class="topo-details"><summary>Topology coordinates (18 regions)</summary>
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
      <td>12</td>
      <td>1</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>34</td>
      <td>14</td>
      <td>34</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>35</td>
      <td>42</td>
      <td>35</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>60</td>
      <td>43</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>63</td>
      <td>61</td>
      <td>63</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>64</td>
      <td>86</td>
      <td>64</td>
      <td>86</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>87</td>
      <td>94</td>
      <td>87</td>
      <td>94</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>95</td>
      <td>120</td>
      <td>95</td>
      <td>120</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>121</td>
      <td>418</td>
      <td>121</td>
      <td>418</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>419</td>
      <td>439</td>
      <td>419</td>
      <td>439</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>440</td>
      <td>448</td>
      <td>440</td>
      <td>448</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>449</td>
      <td>465</td>
      <td>449</td>
      <td>465</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>466</td>
      <td>525</td>
      <td>466</td>
      <td>525</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>526</td>
      <td>543</td>
      <td>526</td>
      <td>543</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>544</td>
      <td>551</td>
      <td>544</td>
      <td>551</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>552</td>
      <td>567</td>
      <td>552</td>
      <td>567</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>568</td>
      <td>759</td>
      <td>568</td>
      <td>759</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>760</td>
      <td>802</td>
      <td>760</td>
      <td>802</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hg6">4HG6</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGQDAPMIVIEGLTSEEPQASPDAVAEAVPAAEVA</span><span class="topo-outside">PWIIPLRPLAETAQVGPLFRLQGQQARAAFRLFLPTEAVGGTLTLAQRSSIDILPESSQIIVRMNDQEIGRFTPRQFGALGAVTM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">PLGEAVRAGDNLVTIEAQHRHRIYCGADAEFDLWTEVDLSQSGVALPAAAIGTEPTSFIAALTAQAESGRPVEIRTPTPPDEATLRTLAQALGRPLPDEALPLALSKPWSAETGPTYARI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TLLPSDADRVSIRRGGDGAVVLVLEHPPEGSPNASLVADLLGATPTLPPPTLPQIPPGRVVTLADMGVDTILTDNRYFNRDIDFQLPDDWLLLASQKAQIGIDYGFAGGLPEGALLLVKV</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">NGTTVRMLPLDRDAAPVKPRLDIRFPARLLHPGPNRLSFESVIPGNPPDQPCPASAGDLMQVLSSTDLEVPPSPRMQMADMARDLAQVTPASVHPATPDGLARTLPFMAAFREVPDAAPV</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">DLTVAGLHDIATVPLNEEGLTPRLLALTLLPST</span><span class="topo-unknown">VSRLVERPATPA</span><span class="topo-outside">GPPANALAPLGAAPGEGVMPPLVESNWSDRAQTFVQATLQPVIQTVRRMLRPGDGNLAEWLATRKGTAMLLAPEP</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       </span>
<span class="topo-line"><span class="topo-outside">GKLWVILGPEAEPARVAEALAMAPRSPGGPRGQVAVLGSDGRWSSWSKPGLLPELREPVSLDNVRSVVGNVASARPPLL</span><span class="topo-membrane">LGGMLGLAWISAAIAVGFV</span><span class="topo-inside">LRTR</span><span class="topo-unknown">RKGLK</span></span>
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
      <td>35</td>
      <td>19</td>
      <td>53</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>36</td>
      <td>513</td>
      <td>54</td>
      <td>531</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>514</td>
      <td>525</td>
      <td>532</td>
      <td>543</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>526</td>
      <td>679</td>
      <td>544</td>
      <td>697</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>680</td>
      <td>698</td>
      <td>698</td>
      <td>716</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>699</td>
      <td>702</td>
      <td>717</td>
      <td>720</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>703</td>
      <td>707</td>
      <td>721</td>
      <td>725</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>

## Biological / Functional Insights

### Periplasmic domain architecture

The periplasmic region of BcsB is primarily formed by two carbohydrate binding domains (CBD1 and CBD2) connected by a disulphide bond between conserved Cys 163 and Cys 430. These are linked to two compact alpha/beta domains (FD1: amino acids 192-303; FD2: amino acids 457-529 and 598-666) that resemble a flavodoxin fold. The repeating structural motif of BcsB therefore contains a CBD linked to an FD domain.

### Membrane anchoring and interface helices

BcsB is anchored to the inner membrane via a single C-terminal transmembrane helix (amino acids 695-720). At the water-lipid interface, BcsB forms two amphipathic helices: IF4 (amino acids 569-592) interacts with the periplasmic termini of BcsA's TM2, TM6, and TM8, while IF5 (amino acids 679-693) directly precedes BcsB's membrane anchor and contacts BcsA's TM1 and the 1/2 loop.

### Conserved residues in CBD1 and glucan interaction

A cluster of conserved residues including His 159, Arg 160, Ile 161, Leu 171, and Trp 172 is located at the tip of CBD1, close to its disulphide bond with CBD2 and above the periplasmic exit of the glucan channel. Comparison of CBD1 with the bacterial carbohydrate binding module family 35 (CBM35) in complex with a glucuronic acid disaccharide localizes disaccharide binding to this cluster of conserved residues, indicating that CBD1 interacts with the translocating glucan.

### BcsA-BcsB complex interface

[Bcsa](/xray-mp-wiki/proteins/enzymes/bcsa/) and BcsB form an elongated complex. BcsB's transmembrane anchor packs against one side of the cuboid arrangement of BcsA's transmembrane helices. BcsA's TM2 and TM3, as well as its 5/6 loop, account for almost 30% of the complex interface with BcsB. The periplasmic exit of the glucan channel is between BcsA's 5/6 and 7/8 loops at the BcsA-BcsB interface, where the glucan kinks to protrude from the complex sideways.


## Cross-References

- <a href="/xray-mp-wiki/proteins/enzymes/bcsa/">BcsA from Rhodobacter sphaeroides</a> — Catalytic partner; BcsA-BcsB complex solved by X-ray crystallography at 4.5 A
- <a href="/xray-mp-wiki/reagents/detergents/triton-x-100/">Triton X-100</a> — Nonionic detergent used for solubilization of BcsA-BcsB complex from membranes
- <a href="/xray-mp-wiki/reagents/buffers/sodium-phosphate/">Sodium Phosphate Buffer</a> — Buffer component in purification buffers
- <a href="/xray-mp-wiki/reagents/additives/cellobiose/">Cellobiose</a> — Additive (5 mM) in purification buffers for BcsA-BcsB complex
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride (MgCl2)</a> — Additive (5 mM) in solubilization buffer
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/gt-a-fold/">GT-A Fold (Glycosyltransferase A Fold)</a> — Structural domain of partner protein BcsA
- <a href="/xray-mp-wiki/concepts/structural-mechanisms/pilz-domain/">PilZ Domain</a> — Cyclic-di-GMP binding domain of partner protein BcsA
- <a href="/xray-mp-wiki/reagents/additives/glucose/">Glucose</a> — Referenced in the context of Glucose
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Mgcl2</a> — Referenced in the context of Mgcl2
- <a href="/xray-mp-wiki/reagents/additives/peg200/">PEG200</a> — Referenced in the context of PEG200
