---
title: "GsuK Multi-Ligand Gated K+ Channel"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [ion-channel, membrane-protein]
sources: [doi/10.7554##eLife.00184]
verified: agent
uniprot_id: Q74FS9
---

# GsuK Multi-Ligand Gated K+ Channel

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q74FS9">UniProt: Q74FS9</a>

<span class="expr-badge">Geobacter sulfurreducens</span>

## Overview

GsuK is a two-transmembrane, RCK-regulated K+ channel from *Geobacter sulfurreducens*. Each subunit contains two tandem RCK domains, reminiscent of Slo K+ channels. The channel is activated by [ADP](/xray-mp-wiki/reagents/ligands/adp/) and NAD+, while Ca2+ serves as an allosteric inhibitor. GsuK features a segmented inner helix pore with a unique opening mechanism distinct from other K+ channels. The channel exhibits weak K+ selectivity due to a Phe residue in the selectivity filter, and its intracellular gate is located at the end of the inner helix, coupled to the RCK gating ring via extended linkers.


## Publications

### doi/10.7554##eLife.00184

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4gvl">4GVL</a></td>
      <td>3.0</td>
      <td>I222</td>
      <td>Intracellular subunit (residues 110-564)</td>
      <td></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4gx5">4GX5</a></td>
      <td>3.7</td>
      <td>C2</td>
      <td>Wild-type full-length (E52A/Q77E mutants)</td>
      <td>Ca2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4gx0">4GX0</a></td>
      <td>2.6</td>
      <td>C2</td>
      <td>L97D mutant full-length</td>
      <td>Ca2+</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4gx1">4GX1</a></td>
      <td>2.8</td>
      <td>C2</td>
      <td>L97D mutant with <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a></td>
      <td><a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a></td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4gx2">4GX2</a></td>
      <td>3.2</td>
      <td>C2</td>
      <td>L97D mutant with NAD+</td>
      <td>NAD+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli BL21(DE3)
- **Construct**: Full-length GsuK (Ala9 with N-terminal MQRGS) in pQE70 vector with C-terminal His-tag and thrombin cleavage site
- **Notes**: Intracellular subunit construct starts at Tyr10 with N-terminal MQ
- **Induction**: 0.4 mM [Iptg](/xray-mp-wiki/reagents/additives/iptg/) at A600 ~0.8, 37°C for 3-4 hr

**Purification:**

- **Expression system**: E. coli BL21(DE3)
- **Expression construct**: GsuK in pQE70 with C-terminal His-tag
- **Tag info**: C-terminal His6, removed by in-gel thrombin digestion

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
      <td>Cell harvest and lysis</td>
      <td>Lysis</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>(/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 250 mM <a href="/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/">KCl</a>, protease inhibitors</td>
      <td></td>
    </tr>
    <tr>
      <td>Membrane protein extraction</td>
      <td>Detergent extraction</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>(/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 250 mM <a href="/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/">KCl</a> + 40 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">N Decyl Beta D Maltoside</a> (DM)</td>
      <td>3 hr at room temperature</td>
    </tr>
    <tr>
      <td>Affinity chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">IMAC (Co2+)</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> Co2+ affinity resin (Clontech)</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a>(/xray-mp-wiki/reagents/buffers/tris/) pH 8.0, 250 mM <a href="/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/">KCl</a> + 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td></td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Thrombin cleavage</td>
      <td>—</td>
      <td></td>
      <td>In-gel digestion, 1 U thrombin per L culture, 4°C overnight</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">[SEC</a> (Size-Exclusion Chromatography)](/xray-mp-wiki/methods/purification/size-exclusion-chromatography/)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> (10/30)</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/ches/">CHES</a> pH 9.0, 150 mM KSCN, 2 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> + 4 mM <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a></td>
      <td>For full-length channel; also contains 0.1 mg/ml <a href="/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/">E. coli Polar Lipids</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: ~6-8 mg/ml in SEC buffer
**Purity**: Tetrameric on SEC

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified GsuK intracellular subunit (~8 mg/ml)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20-23% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 3350, 120 mM <a href="/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/">KCl</a>, 80 mM NaNO3, 1% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/bis-tris-propane/">Bis-Tris propane</a> pH 8.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 400</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Intracellular subunit crystals</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting Drop Vapor Diffusion</a></td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Full-length GsuK in <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> with <a href="/xray-mp-wiki/reagents/lipids/e-coli-polar-lipids/">E. coli Polar Lipids</a> (~6 mg/ml)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>20-23% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 3350, 120 mM <a href="/xray-mp-wiki/reagents/additives/potassium-chloride-kcl/">KCl</a>, 80 mM NaNO3, 1% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 100 mM <a href="/xray-mp-wiki/reagents/buffers/bis-tris-propane/">Bis-Tris propane</a> pH 8.5</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/peg/">Peg</a> 400</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Full-length channel crystals; various constructs used (wild-type, L97D, L97D+<a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a>, L97D+NAD+)</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx5">4GX5</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-outside">QNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSF</span><span class="topo-unknown">MAGIYWTITVMTTLGF</span><span class="topo-inside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLLIILPFGFVSMF</span><span class="topo-outside">LAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATT</span><span class="topo-unknown">CGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAP</span><span class="topo-outside">EDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHK</span><span class="topo-unknown">ESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-unknown">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAARLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>17</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>42</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>68</td>
      <td>56</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>105</td>
      <td>83</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>258</td>
      <td>109</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>346</td>
      <td>262</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>477</td>
      <td>350</td>
      <td>480</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>478</td>
      <td>565</td>
      <td>481</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx5">4GX5</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRA</span><span class="topo-outside">RQNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSF</span><span class="topo-unknown">MAGIYWTITVMTTLGF</span><span class="topo-inside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLLIILPFGFVSMF</span><span class="topo-outside">LAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATTCGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAPEDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-outside">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAAR</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>13</td>
      <td>4</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>17</td>
      <td>17</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>42</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>68</td>
      <td>56</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>105</td>
      <td>83</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>561</td>
      <td>109</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>565</td>
      <td>565</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx5">4GX5</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-outside">QNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSF</span><span class="topo-unknown">MAGIYWTITVMTTLGF</span><span class="topo-inside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLLIILPFGFVSMF</span><span class="topo-outside">LAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATT</span><span class="topo-unknown">CGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAP</span><span class="topo-outside">EDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHK</span><span class="topo-unknown">ESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-unknown">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAARLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>17</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>42</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>68</td>
      <td>56</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>105</td>
      <td>83</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>258</td>
      <td>109</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>346</td>
      <td>262</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>477</td>
      <td>350</td>
      <td>480</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>478</td>
      <td>565</td>
      <td>481</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx5">4GX5</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRA</span><span class="topo-outside">RQNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSF</span><span class="topo-unknown">MAGIYWTITVMTTLGF</span><span class="topo-inside">GDITFESDA</span><span class="topo-membrane">GYLFASIVTVSGVIFLLIILPFGFVSMF</span><span class="topo-outside">LAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATTCGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAPEDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-outside">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAAR</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>13</td>
      <td>4</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>17</td>
      <td>17</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>42</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>68</td>
      <td>56</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>77</td>
      <td>72</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>105</td>
      <td>81</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>106</td>
      <td>561</td>
      <td>109</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>565</td>
      <td>565</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx0">4GX0</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-outside">QNLK</span><span class="topo-membrane">VLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSFMAG</span><span class="topo-unknown">IYWTITVMTTLGF</span><span class="topo-inside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLDIILPFGF</span><span class="topo-outside">VSMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATT</span><span class="topo-unknown">CGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAP</span><span class="topo-outside">EDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHK</span><span class="topo-unknown">ESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-unknown">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAARLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>18</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>38</td>
      <td>22</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>42</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>68</td>
      <td>59</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>83</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>258</td>
      <td>105</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>346</td>
      <td>262</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>477</td>
      <td>350</td>
      <td>480</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>478</td>
      <td>565</td>
      <td>481</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx0">4GX0</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-outside">QNLK</span><span class="topo-membrane">VLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSFMAG</span><span class="topo-unknown">IYWTITVMTTLGF</span><span class="topo-inside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLDIILPFGF</span><span class="topo-outside">VSMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATTCGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAPEDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-outside">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAAR</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>18</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>38</td>
      <td>22</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>42</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>68</td>
      <td>59</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>83</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>561</td>
      <td>105</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>565</td>
      <td>565</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx0">4GX0</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-outside">QNLK</span><span class="topo-membrane">VLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSFMAG</span><span class="topo-unknown">IYWTITVMTTLGF</span><span class="topo-inside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLDIILPFGF</span><span class="topo-outside">VSMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATT</span><span class="topo-unknown">CGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAP</span><span class="topo-outside">EDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHK</span><span class="topo-unknown">ESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-unknown">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAARLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>18</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>38</td>
      <td>22</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>42</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>68</td>
      <td>59</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>83</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>258</td>
      <td>105</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>346</td>
      <td>262</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>477</td>
      <td>350</td>
      <td>480</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>478</td>
      <td>565</td>
      <td>481</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx0">4GX0</a> — Chain G (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-outside">QNLK</span><span class="topo-membrane">VLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSFMAG</span><span class="topo-unknown">IYWTITVMTTLGF</span><span class="topo-inside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLDIILPFGF</span><span class="topo-outside">VSMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATTCGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAPEDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-outside">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAAR</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>18</td>
      <td>18</td>
      <td>21</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>19</td>
      <td>38</td>
      <td>22</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>42</td>
      <td>58</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>68</td>
      <td>59</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>101</td>
      <td>83</td>
      <td>104</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>561</td>
      <td>105</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>565</td>
      <td>565</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx1">4GX1</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-inside">QNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-outside">RYLMWHLEGRAYSFMAG</span><span class="topo-unknown">IYWTITVMTTLGF</span><span class="topo-outside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLDIILPFGFV</span><span class="topo-inside">SMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VVPLTRILGRYLGIRATT</span><span class="topo-unknown">CGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAP</span><span class="topo-inside">EDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKE</span><span class="topo-unknown">SA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-unknown">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAARLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>17</td>
      <td>18</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>42</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>68</td>
      <td>59</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>102</td>
      <td>83</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>258</td>
      <td>106</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>346</td>
      <td>262</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>478</td>
      <td>350</td>
      <td>481</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>479</td>
      <td>565</td>
      <td>482</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx1">4GX1</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-inside">QNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-outside">RYLMWHLEGRAYSFMAG</span><span class="topo-unknown">IYWTITVMTTLGF</span><span class="topo-outside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLDIILPFGFV</span><span class="topo-inside">SMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VVPLTRILGRYLGIRATTCGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAPEDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-inside">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAAR</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>17</td>
      <td>18</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>42</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>68</td>
      <td>59</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>102</td>
      <td>83</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>561</td>
      <td>106</td>
      <td>564</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>565</td>
      <td>565</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx1">4GX1</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-inside">QNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-outside">RYLMWHLEGRAYSFMAG</span><span class="topo-unknown">IYWTITVMTTLGF</span><span class="topo-outside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLDIILPFGFV</span><span class="topo-inside">SMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VVPLTRILGRYLGIRATT</span><span class="topo-unknown">CGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAP</span><span class="topo-inside">EDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKE</span><span class="topo-unknown">SA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-unknown">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAARLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>17</td>
      <td>18</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>42</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>68</td>
      <td>59</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>102</td>
      <td>83</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>258</td>
      <td>106</td>
      <td>261</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>346</td>
      <td>262</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>478</td>
      <td>350</td>
      <td>481</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>479</td>
      <td>565</td>
      <td>482</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx1">4GX1</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-inside">QNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-outside">RYLMWHLEGRAYSFMAG</span><span class="topo-unknown">IYWTITVMTTLGF</span><span class="topo-outside">GDITFESDAGY</span><span class="topo-membrane">LFASIVTVSGVIFLDIILPFGFV</span><span class="topo-inside">SMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VVPLTRILGRYLGIRATTCGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAPEDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-inside">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAAR</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>17</td>
      <td>18</td>
      <td>20</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>55</td>
      <td>42</td>
      <td>58</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>56</td>
      <td>68</td>
      <td>59</td>
      <td>71</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>72</td>
      <td>82</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>102</td>
      <td>83</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>561</td>
      <td>106</td>
      <td>564</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>565</td>
      <td>565</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx2">4GX2</a> — Chain A (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-outside">QNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSF</span><span class="topo-unknown">MAGIYWTITVMTTLGFG</span><span class="topo-inside">DITFESDA</span><span class="topo-membrane">GYLFASIVTVSGVIFLDIILPFGFV</span><span class="topo-outside">SMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATT</span><span class="topo-unknown">CGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAP</span><span class="topo-outside">EDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHK</span><span class="topo-unknown">ESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-unknown">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAARLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>17</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>42</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>69</td>
      <td>56</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>70</td>
      <td>77</td>
      <td>73</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>81</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>258</td>
      <td>106</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>346</td>
      <td>262</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>477</td>
      <td>350</td>
      <td>480</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>478</td>
      <td>565</td>
      <td>481</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx2">4GX2</a> — Chain B (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRA</span><span class="topo-outside">RQNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSF</span><span class="topo-unknown">MAGIYWTITVMTTLGFG</span><span class="topo-inside">DITFESDA</span><span class="topo-membrane">GYLFASIVTVSGVIFLDIILPFGFV</span><span class="topo-outside">SMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATTCGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAPEDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-outside">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAAR</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>13</td>
      <td>4</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>17</td>
      <td>17</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>42</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>69</td>
      <td>56</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>70</td>
      <td>77</td>
      <td>73</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>81</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>561</td>
      <td>106</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>565</td>
      <td>565</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx2">4GX2</a> — Chain E (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRAR</span><span class="topo-outside">QNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSF</span><span class="topo-unknown">MAGIYWTITVMTTLGFG</span><span class="topo-inside">DITFESDA</span><span class="topo-membrane">GYLFASIVTVSGVIFLDIILPFGFV</span><span class="topo-outside">SMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATT</span><span class="topo-unknown">CGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAP</span><span class="topo-outside">EDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHK</span><span class="topo-unknown">ESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-unknown">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAARLVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (11 regions)</summary>
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
      <td>14</td>
      <td>4</td>
      <td>17</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>17</td>
      <td>18</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>42</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>69</td>
      <td>56</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>70</td>
      <td>77</td>
      <td>73</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>81</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>258</td>
      <td>106</td>
      <td>261</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>259</td>
      <td>346</td>
      <td>262</td>
      <td>349</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>347</td>
      <td>477</td>
      <td>350</td>
      <td>480</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>478</td>
      <td>565</td>
      <td>481</td>
      <td>568</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4gx2">4GX2</a> — Chain F (2 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQRGSAYFLRGRA</span><span class="topo-outside">RQNL</span><span class="topo-membrane">KVLLLYCAFLLVMLLAYASIF</span><span class="topo-inside">RYLMWHLEGRAYSF</span><span class="topo-unknown">MAGIYWTITVMTTLGFG</span><span class="topo-inside">DITFESDA</span><span class="topo-membrane">GYLFASIVTVSGVIFLDIILPFGFV</span><span class="topo-outside">SMFLAPWIERRLRYHPTI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">ELPDDTRGHILIFGIDPITRTLIRKLESRNHLFVVVTDNYDQALHLEEQEGFKVVYGSPTDAHVLAGLRVAAARSIIANLSDPDNANLCLTVRSLCQTPIIAVVKEPVHGELLRLAGANQ</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">VVPLTRILGRYLGIRATTCGALAHILDSFGNLQIAELPVHGTPFAGKTIGESGIRQRTGLSIIGVWERGSLTTPQRETVLTEQSLLVLAGTKSQLAALEYLIGEAPEDELIFIIGHGRIG</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">CAAAAFLDRKPVPFILIDRQESPVCNDHVVVYGDATVGQTLRQAGIDRASGIIVTTNDDSTNIFLTLACRHLHSHIRIVARANGEENVDQLYAAGADFVVSNASVGANILGNLLEHKESA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560     </span>
<span class="topo-line"><span class="topo-outside">FLSEGMAVFRRPLPPAMAGKTIAETRLRPLTGCSIVAIEAPDRADILISPPPETILAEGARLILIGTSEQEKTFDQTIAAR</span><span class="topo-unknown">LVPR</span></span>
<details class="topo-details"><summary>Topology coordinates (9 regions)</summary>
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
      <td>13</td>
      <td>4</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>14</td>
      <td>17</td>
      <td>17</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>18</td>
      <td>38</td>
      <td>21</td>
      <td>41</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>52</td>
      <td>42</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>53</td>
      <td>69</td>
      <td>56</td>
      <td>72</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>70</td>
      <td>77</td>
      <td>73</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>78</td>
      <td>102</td>
      <td>81</td>
      <td>105</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>103</td>
      <td>561</td>
      <td>106</td>
      <td>564</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>562</td>
      <td>565</td>
      <td>565</td>
      <td>568</td>
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

### Multi-ligand gating mechanism

GsuK is activated by [ADP](/xray-mp-wiki/reagents/ligands/adp/) and NAD+ and inhibited by Ca2+. Ca2+ binds at the inter-subunit assembly interface of the gating ring, stabilizing the closed conformation. [ADP](/xray-mp-wiki/reagents/ligands/adp/) binds at the Rossmann-fold nucleotide binding site on RCK2; the cis configuration of [ADP](/xray-mp-wiki/reagents/ligands/adp/) inserts the beta-phosphate into a pocket at the flexible interface, promoting gating ring conformational change. NAD+ binds with the nicotinamide group inserted beneath the alphaF helix of RCK1, acting as a lever to promote hinged motion.

### Distinct pore opening mechanics

GsuK has a segmented inner helix (TM2A, TM2B, TM2C) with two hinge points (Gly92 and between TM2B/2C). The intracellular gate is at Leu117, at the end of the inner helix, coupled directly to the gating ring via extended linkers. Pore opening involves bending at Gly92 (hinge 1) with TM2B and TM2C moving as a rigid body, rotating Leu117 away from the permeation pathway — a mechanism distinct from [Mthk](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/) and Kv channels.

### Structural resemblance to Slo channels

GsuK shares several features with eukaryotic Slo K+ channels: dual RCK domains per subunit, TVGFG selectivity filter sequence, segmented inner helix with a proline break equivalent, and NAD+ modulation at the conserved nucleotide binding site in RCK2. The relative orientation between the pore and gating ring in GsuK may more closely resemble Slo channels than [Mthk](/xray-mp-wiki/proteins/voltage-gated-channels/mthk/).


## Cross-References

- <a href="/xray-mp-wiki/concepts/structural-mechanisms/rck-domain-activation-mechanism/">RCK Domain Activation Mechanism</a> — GsuK gating is regulated by its RCK domains binding ADP, NAD+, and Ca2+
- <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP</a> — Referenced in gsuk text
- <a href="/xray-mp-wiki/reagents/additives/iptg/">Iptg</a> — Referenced in gsuk text
- <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris</a> — Referenced in gsuk text
- <a href="/xray-mp-wiki/reagents/detergents/dm/">N Decyl Beta D Maltoside</a> — Referenced in gsuk text
- <a href="/xray-mp-wiki/reagents/additives/talon/">Talon</a> — Referenced in gsuk text
- <a href="/xray-mp-wiki/reagents/detergents/dm/">DM</a> — Referenced in gsuk text
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Referenced in gsuk text
- <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> — Referenced in gsuk text
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Referenced in gsuk text
