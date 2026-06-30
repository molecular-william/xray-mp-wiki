---
title: "Na+,K+-ATPase (Pig Kidney)"
created: 2026-05-27
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature06419, doi/10.1016##j.jsb.2010.12.004, doi/10.1016##j.jbc.2022.102317, doi/10.1073##pnas.1222308110, doi/10.1073##pnas.1422997112, doi/10.1126##science.1243352, doi/10.1073##pnas.2020438118]
verified: false
---

# Na+,K+-ATPase (Pig Kidney)

## Overview

The Na+,K+-ATPase is a P-type ATPase pump that maintains the electrochemical gradient across animal cell membranes by transporting three Na+ ions out and two K+ ions into the cell per ATP hydrolyzed. It is a housekeeping enzyme essential for secondary solute transport, cell excitability, and cell volume regulation. The minimal functional unit consists of a catalytic alpha subunit and a beta subunit acting as chaperone, with a regulatory gamma subunit from the FXYD family often present in a tissue-specific manner. The first crystal structure of the pig kidney Na+,K+-ATPase was solved in the E2-MgF4(2-)-2K+ state (PDB 3B8E), revealing the architecture of the alpha-beta-gamma complex. High-affinity [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) binding was captured in the E2P phosphoenzyme state, and the E2-BeFx phosphorylated intermediate state was studied for cation occlusion and dephosphorylation transitions. A 3.4 A structure of the [Mg]E2P-[Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) complex revealed Mg2+ bound at cation site II and provided detailed insight into cardiotonic steroid recognition.


## Publications

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1038##nature06419 (1 structure, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3b8e">3B8E</a></td>
      <td>3.5</td>
      <td>P 1 21 1</td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma (FXYD2) subunits in E2-MgF4(2-)-2K+ state</td>
      <td>MgF4(2-), K+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pig (Sus scrofa) kidney cortex, native extraction
- **Construct**: Native Na+,K+-ATPase from pig kidney outer medulla; no heterologous expression tags or mutations

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
      <td>Native extraction</td>
      <td>Native extraction from pig kidney outer medulla</td>
      <td>—</td>
      <td></td>
      <td>Specific ATPase activity of the preparation was about 1800 umol Pi/h per mg of protein at 37 C</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified pig kidney Na+,K+-ATPase solubilized in <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> pH 7.0, 12.5% <a href="/xray-mp-wiki/reagents/additives/peg/">PEG</a> 4000, 20% 2-propanol, 0.2 M NaCl</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>First crystal structure of Na+,K+-ATPase in E2-MgF4(2-)-2K+ state. Space group P21.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3b8e">3B8E</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">AKKERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTPEWVKFCRQ</span><span class="topo-membrane">LFGGFSMLLWIGAILCFLAYG</span><span class="topo-outside">IQAATEEEPQN</span><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">F</span><span class="topo-inside">SYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFSTNCVEGTARGIVVYTGDRT</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VMGRIATLASGLEGGQTPIAAEIEHF</span><span class="topo-membrane">IHIITGVAVFLGVSFFILSLI</span><span class="topo-outside">LEYTWL</span><span class="topo-membrane">EAVIFLIGIIVANVPEGLLAT</span><span class="topo-inside">VTVCLTLTAKRMARKNCLVKNLEAVETLGSTSTICSDKTGTLTQNR</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">MTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNKYQLSIHKNPNTAEPRHLL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">VMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCRSAGIKVIMVTGDHPITAK</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">AIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKKADIGVAMGIAGSDVSKQA</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">ADMILLDDNFASIVTGVEEGRLIFDNLKK</span><span class="topo-membrane">SIAYTLTSNIPEITPFLIFII</span><span class="topo-outside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAISL</span><span class="topo-inside">AYEQAESDIMKRQPRNPKTDKLVNE</span><span class="topo-membrane">QLISMAYGQIGMIQALGG</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-membrane">FFTY</span><span class="topo-outside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVICK</span><span class="topo-inside">TRRNSVFQQGM</span><span class="topo-membrane">KNKILIFGLFEETALAAFLSYCP</span><span class="topo-outside">GMGVALRMYPLKP</span></span>
<span class="topo-ruler">       970       980       990        </span>
<span class="topo-line"><span class="topo-outside">TWW</span><span class="topo-membrane">FCAFPYSLLIFVYDEVRKLI</span><span class="topo-inside">IRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (21 regions)</summary>
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
      <td>70</td>
      <td>19</td>
      <td>88</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>91</td>
      <td>89</td>
      <td>109</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>102</td>
      <td>110</td>
      <td>120</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>103</td>
      <td>121</td>
      <td>121</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>266</td>
      <td>140</td>
      <td>284</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>267</td>
      <td>287</td>
      <td>285</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>293</td>
      <td>306</td>
      <td>311</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>294</td>
      <td>314</td>
      <td>312</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>749</td>
      <td>333</td>
      <td>767</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>750</td>
      <td>770</td>
      <td>768</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>771</td>
      <td>776</td>
      <td>789</td>
      <td>794</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>777</td>
      <td>797</td>
      <td>795</td>
      <td>815</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>798</td>
      <td>822</td>
      <td>816</td>
      <td>840</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>823</td>
      <td>844</td>
      <td>841</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>845</td>
      <td>894</td>
      <td>863</td>
      <td>912</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>913</td>
      <td>913</td>
      <td>931</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>914</td>
      <td>924</td>
      <td>932</td>
      <td>942</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>925</td>
      <td>947</td>
      <td>943</td>
      <td>965</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>948</td>
      <td>963</td>
      <td>966</td>
      <td>981</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>964</td>
      <td>983</td>
      <td>982</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>984</td>
      <td>998</td>
      <td>1002</td>
      <td>1016</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3b8e">3B8E</a> — Chain D (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40      </span>
<span class="topo-line"><span class="topo-inside">TGGS</span><span class="topo-membrane">WFKILLFYVIFYGCLAGIFIGT</span><span class="topo-outside">IQVMLLTISEFKPTYQDRVA</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>28</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>26</td>
      <td>32</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>46</td>
      <td>54</td>
      <td>73</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3b8e">3B8E</a> — Chain H (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20         </span>
<span class="topo-line"><span class="topo-outside">YETVRNG</span><span class="topo-membrane">GLIFAALAFIVGLIIILSK</span><span class="topo-inside">RLR</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>7</td>
      <td>23</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>8</td>
      <td>26</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>29</td>
      <td>49</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##j.jsb.2010.12.004 (1 structure, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3n23">3N23</a></td>
      <td>4.6</td>
      <td>P 21 21 21</td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma (FXYD) subunits in E2P phosphoenzyme state</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a> (one molecule per alpha subunit)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pig (Sus scrofa) kidney cortex, native extraction
- **Construct**: Native Na+,K+-ATPase from pig kidney outer medulla; no heterologous expression tags or mutations

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>E2P phosphoenzyme formation followed by <a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a> stabilization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified pig kidney Na+,K+-ATPase</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>Phosphoenzyme formed by Pi-induced phosphorylation in the presence of Mg2+</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>E2P state induced by inorganic phosphate phosphorylation in the presence of Mg2+, yielding high affinity <a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a> binding (type II complex). Space group P212121, type I crystal packing through stacked lipid-detergent bilayers.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3n23">3N23</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTPE</span><span class="topo-unknown">WVKFCRQL</span><span class="topo-inside">FGGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQ</span><span class="topo-outside">AATEEEPQ</span><span class="topo-membrane">NDNLYLGVVLSAVVIIT</span><span class="topo-inside">GCFSYYQE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">AKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFSTNCVEGTARGIVVYTGDRTVMGRIA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">TLASGLEGGQTPIAAEIEHFIHI</span><span class="topo-membrane">ITGVAVFLGVSFFILSLI</span><span class="topo-outside">LEYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-inside">VTVCLTLTAKRMARKNCLVKNLEAVETLGSTSTICSDKTGTLTQNRMTVAHM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">WSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNKYQLSIHKNPNTAEPRHLLVMKGAP</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">ERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCRSAGIKVIMVTGDHPITAKAIAKGV</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">GIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKKADIGVAMGIAGSDVSKQAADMILL</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">DDNFASIVTGVEEGRLIFDNLKKSI</span><span class="topo-membrane">AYTLTSNIPEITPFLIFII</span><span class="topo-outside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAI</span><span class="topo-inside">SLAYEQAESDIMKRQPRNPKTDKLVNEQLI</span><span class="topo-membrane">SMAYGQIGMIQALGGFFTY</span><span class="topo-outside">FV</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">ILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-inside">KTRRNSVFQQGMKNKIL</span><span class="topo-membrane">IFGLFEETALAAFLSYC</span><span class="topo-outside">PGMGVALRMYPLKPTW</span><span class="topo-membrane">WFCA</span></span>
<span class="topo-ruler">       970       980       990  </span>
<span class="topo-line"><span class="topo-membrane">FPYSLLIFVYDEVR</span><span class="topo-inside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>57</td>
      <td>25</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>58</td>
      <td>65</td>
      <td>82</td>
      <td>89</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>66</td>
      <td>69</td>
      <td>90</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>87</td>
      <td>94</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>88</td>
      <td>95</td>
      <td>112</td>
      <td>119</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>96</td>
      <td>112</td>
      <td>120</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>263</td>
      <td>137</td>
      <td>287</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>281</td>
      <td>288</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>282</td>
      <td>286</td>
      <td>306</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>308</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>309</td>
      <td>745</td>
      <td>333</td>
      <td>769</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>746</td>
      <td>764</td>
      <td>770</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>765</td>
      <td>770</td>
      <td>789</td>
      <td>794</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>771</td>
      <td>789</td>
      <td>795</td>
      <td>813</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>790</td>
      <td>819</td>
      <td>814</td>
      <td>843</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>820</td>
      <td>838</td>
      <td>844</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>839</td>
      <td>888</td>
      <td>863</td>
      <td>912</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>889</td>
      <td>906</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>907</td>
      <td>923</td>
      <td>931</td>
      <td>947</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>924</td>
      <td>940</td>
      <td>948</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>941</td>
      <td>956</td>
      <td>965</td>
      <td>980</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>957</td>
      <td>974</td>
      <td>981</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>975</td>
      <td>992</td>
      <td>999</td>
      <td>1016</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3n23">3N23</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">RTGGSW</span><span class="topo-membrane">FKILLFYVIFYGCLAGIFIGTI</span><span class="topo-outside">QVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDDMIFEDCGNVPSELKERGEYNNERGER</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">KVCRFRLEWLGNC</span><span class="topo-unknown">SGLNDETY</span><span class="topo-outside">GYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTG</span><span class="topo-unknown">KRDED</span><span class="topo-outside">KEKVGTMEYFGLGGYPGFPLQYYPYYGKLLQPKYLQPLMAVQFTNL</span></span>
<span class="topo-ruler">       250       260       270       </span>
<span class="topo-line"><span class="topo-outside">TMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
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
      <td>6</td>
      <td>27</td>
      <td>32</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>28</td>
      <td>33</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>133</td>
      <td>55</td>
      <td>159</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>134</td>
      <td>141</td>
      <td>160</td>
      <td>167</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>142</td>
      <td>189</td>
      <td>168</td>
      <td>215</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>190</td>
      <td>194</td>
      <td>216</td>
      <td>220</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>195</td>
      <td>277</td>
      <td>221</td>
      <td>303</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3n23">3N23</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30 </span>
<span class="topo-line"><span class="topo-outside">DPFYYDYETVRNG</span><span class="topo-membrane">GLIFAALAFIVGLIIIL</span><span class="topo-inside">S</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>30</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>31</td>
      <td>31</td>
      <td>47</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1016##j.jbc.2022.102317 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7qtv">7QTV</a></td>
      <td>4.0</td>
      <td>P 21 21 21</td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma (FXYD2) subunits in E2-BeFx phosphorylated intermediate state</td>
      <td>BeFx (beryllium fluoride), Mg2+</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pig (Sus scrofa) kidney cortex, native extraction
- **Construct**: Native Na+,K+-ATPase from pig kidney outer medulla; no heterologous expression tags or mutations

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>9-10 mg/mL E2-BeFx complex in 20 mM histidine pH 7.0, 10 mM NaF, 0.5 mM MgCl2, 20 uM BeSO4, <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a> (0.9 mg/mg protein)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>16.5% <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> monomethyl ether, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 175 mM MgCl2, 150 mM NaCl, 20 mM HEPES/MES pH 6.2, 2 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>15</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-3 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Dehydrated overnight at 4 C against 30% <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> MME reservoir; flash-cooled at 100 K</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>E2-BeFx complex. Anisotropic data truncated to 5.4, 4.4, 4.0 A along a*, b*, c*. Rb+ soaks performed for occlusion studies.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7qtv">7QTV</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKGVGRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTPEWVKF</span><span class="topo-membrane">CRQLFGGFSMLLWIGAILCFLAYGIQ</span><span class="topo-inside">AATE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EEPQN</span><span class="topo-membrane">DNLYLGVVLSAVVIITGCFS</span><span class="topo-outside">YYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AFFSTNCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEI</span><span class="topo-membrane">EHFIHIITGVAVFLGVSFFILSLI</span><span class="topo-inside">LEYTWLEA</span><span class="topo-membrane">VIFLIGIIVANVPEGLLATVTV</span><span class="topo-outside">CLTLTAKRMARKNCLVKNLE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AVETLGSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPF</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">NSTNKYQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">VGKCRSAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">PASKKADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLK</span><span class="topo-membrane">KSIAYTLTSNIPEITPFLIF</span><span class="topo-inside">IIANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAISL</span><span class="topo-outside">AYEQAESDIMKRQPRNPKTD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">KLV</span><span class="topo-membrane">NEQLISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVICK</span><span class="topo-outside">TRRNSVFQQGMKNK</span><span class="topo-membrane">ILIFGLFEET</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020 </span>
<span class="topo-line"><span class="topo-membrane">ALAAFLSYCP</span><span class="topo-inside">GMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVRKLI</span><span class="topo-outside">IRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>25</td>
      <td>-4</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>90</td>
      <td>21</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>116</td>
      <td>86</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>125</td>
      <td>112</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>126</td>
      <td>145</td>
      <td>121</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>286</td>
      <td>141</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>310</td>
      <td>282</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>318</td>
      <td>306</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>319</td>
      <td>340</td>
      <td>314</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>771</td>
      <td>336</td>
      <td>766</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>772</td>
      <td>791</td>
      <td>767</td>
      <td>786</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>792</td>
      <td>799</td>
      <td>787</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>800</td>
      <td>820</td>
      <td>795</td>
      <td>815</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>821</td>
      <td>843</td>
      <td>816</td>
      <td>838</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>844</td>
      <td>867</td>
      <td>839</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>868</td>
      <td>917</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>918</td>
      <td>936</td>
      <td>913</td>
      <td>931</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>937</td>
      <td>950</td>
      <td>932</td>
      <td>945</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>951</td>
      <td>970</td>
      <td>946</td>
      <td>965</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>971</td>
      <td>983</td>
      <td>966</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>984</td>
      <td>1006</td>
      <td>979</td>
      <td>1001</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1007</td>
      <td>1021</td>
      <td>1002</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7qtv">7QTV</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKE</span><span class="topo-membrane">FLGRTGGSWFKILLFYVIFYGCLAGIFIGTI</span><span class="topo-inside">QVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>13</td>
      <td>23</td>
      <td>13</td>
      <td>23</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>24</td>
      <td>54</td>
      <td>24</td>
      <td>54</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>55</td>
      <td>303</td>
      <td>55</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7qtv">7QTV</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETV</span><span class="topo-membrane">RNGGLIFAALAFIVGLIIILS</span><span class="topo-outside">K</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>26</td>
      <td>17</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>47</td>
      <td>27</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>48</td>
      <td>48</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7qtv">7QTV</a> — Chain E (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-outside">DPFYYDYETVRNG</span><span class="topo-membrane">GLIFAALAFIVGLIIILSK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>29</td>
      <td>17</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>48</td>
      <td>30</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.1222308110 (1 structure, 4 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4hyt">4HYT</a></td>
      <td>3.4</td>
      <td>P 21 21 21</td>
      <td>Phosphorylated pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in [Mg]E2P-<a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a> high-affinity complex</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a>, Mg2+ (bound at cation site II)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pig (Sus scrofa) kidney cortex, native extraction
- **Construct**: Native Na+,K+-ATPase from pig kidney outer medulla; no heterologous expression tags or mutations

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
      <td>Membrane preparation</td>
      <td>Large-scale preparation from pig kidney outer medulla</td>
      <td>—</td>
      <td></td>
      <td>As described by Klodos et al. (2002)</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td><a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a> at 0.9 mg per mg protein</td>
      <td>Insoluble material removed by ultracentrifugation</td>
    </tr>
  </tbody>
</table>
**Final sample**: 9-10 mg/mL solubilized protein

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion, hanging drop</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>9-10 mg/mL solubilized Na+,K+-ATPase with 1.6 mM <a href="/xray-mp-wiki/reagents/ligands/sucrose/">Sucrose</a> monodecanoate and 5 mM <a href="/xray-mp-wiki/reagents/additives/dtt/">DTT</a> added</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>16-17% <a href="/xray-mp-wiki/reagents/additives/peg2000/">PEG 2000</a> MME, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 200 mM MgCl2, 100 mM MES (titrated with <a href="/xray-mp-wiki/reagents/additives/n-methyl-d-glucamine/">NMG</a>, pH 6.2), 100 mM <a href="/xray-mp-wiki/reagents/substrates/urea/">UREA</a>, 5% <a href="/xray-mp-wiki/reagents/additives/tert-butanol/">tert-Butanol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>19</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>A few days to 2-3 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Additional 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> for 1 h; flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals up to 150 x 300 x 100 um3. Space group P212121, a=117.2, b=118.1, c=495.3 A, two alphabeta-gamma heterotrimers per asymmetric unit, solvent content 77%. Data collected at Swiss Light Source X06SA and X06DA at 100 K. Anisotropic data truncated to 3.9, 3.9, 3.4 A. <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with PDB 3N23. Refined in PHENIX.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hyt">4HYT</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKGVGRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTPEWVKFCRQLFGGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EEP</span><span class="topo-membrane">QNDNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AFFSTNCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLI</span><span class="topo-inside">LEYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AVETLGSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPF</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">NSTNKYQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">VGKCRSAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">PASKKADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLI</span><span class="topo-inside">FIIANIPLPL</span><span class="topo-membrane">GTVTILCIDLGTDMVPAISL</span><span class="topo-outside">AYEQAESDIMKRQPRNPKTD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">KLVNE</span><span class="topo-membrane">QLISMAYGQIGMIQALGGFFT</span><span class="topo-inside">YFVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVICK</span><span class="topo-outside">TRRNSVFQQGMKNK</span><span class="topo-membrane">ILIFGLFEET</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020 </span>
<span class="topo-line"><span class="topo-membrane">ALAAFLSYC</span><span class="topo-inside">PGMGVALRMYPLKPTWW</span><span class="topo-membrane">FCAFPYSLLIFVYDEVRKL</span><span class="topo-outside">IIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>25</td>
      <td>-4</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>98</td>
      <td>21</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>117</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>123</td>
      <td>113</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>143</td>
      <td>119</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>144</td>
      <td>290</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>310</td>
      <td>286</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>306</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>337</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>338</td>
      <td>773</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>774</td>
      <td>790</td>
      <td>769</td>
      <td>785</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>791</td>
      <td>800</td>
      <td>786</td>
      <td>795</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>801</td>
      <td>820</td>
      <td>796</td>
      <td>815</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>821</td>
      <td>845</td>
      <td>816</td>
      <td>840</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>846</td>
      <td>866</td>
      <td>841</td>
      <td>861</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>867</td>
      <td>917</td>
      <td>862</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>918</td>
      <td>936</td>
      <td>913</td>
      <td>931</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>937</td>
      <td>950</td>
      <td>932</td>
      <td>945</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>951</td>
      <td>969</td>
      <td>946</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>970</td>
      <td>986</td>
      <td>965</td>
      <td>981</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>987</td>
      <td>1005</td>
      <td>982</td>
      <td>1000</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1006</td>
      <td>1021</td>
      <td>1001</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hyt">4HYT</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSWKK</span><span class="topo-outside">FIWNSEKKEFLGRTGGS</span><span class="topo-membrane">WFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>1</td>
      <td>14</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>15</td>
      <td>31</td>
      <td>15</td>
      <td>31</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>53</td>
      <td>32</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hyt">4HYT</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRNG</span><span class="topo-membrane">GLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>29</td>
      <td>17</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hyt">4HYT</a> — Chain E (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-outside">DPFYYDYETVRNG</span><span class="topo-membrane">GLIFAALAFIVGLIIIL</span><span class="topo-inside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>29</td>
      <td>17</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>46</td>
      <td>30</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.1422997112 (2 structures, 6 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4res">4RES</a></td>
      <td>3.9</td>
      <td>P 21 21 21</td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P form in complex with <a href="/xray-mp-wiki/reagents/ligands/digoxin/">Digoxin</a> (anisotropically truncated to 5.2, 4.3, 3.9 A along a*, b*, c*)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/digoxin/">Digoxin</a> (trisaccharide-conjugated cardenolide), Mg2+ (bound at cation site II)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4res">4RES</a></td>
      <td>3.4</td>
      <td>P 21</td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P form in complex with <a href="/xray-mp-wiki/reagents/ligands/bufalin/">Bufalin</a> (anisotropically truncated to 5.6, 4.1, 3.4 A along a*, b*, c*)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bufalin/">Bufalin</a> (nonglycosylated bufadienolide), K+ (bound at cation sites I and II)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pig (Sus scrofa) kidney cortex, native extraction
- **Construct**: Native Na+,K+-ATPase from pig kidney outer medulla; no heterologous expression tags or mutations

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified pig kidney Na+,K+-ATPase in <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a>, E2P form with <a href="/xray-mp-wiki/reagents/ligands/digoxin/">Digoxin</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>K+-depleted condition similar to <a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a> complex crystallization</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>19</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Additional <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>; flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>E2P-<a href="/xray-mp-wiki/reagents/ligands/digoxin/">Digoxin</a> complex. Space group P212121, a=118.2, b=118.3, c=494.1 A, two alphabeta-gamma heterotrimers per asymmetric unit. Anisotropic data truncated to 5.2, 4.3, 3.9 A. <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with PDB 4HYT (E2P-<a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a>). Rwork/Rfree=22.1/25.3%. Data collected at Swiss Light Source X06SA at 100 K.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified pig kidney Na+,K+-ATPase in <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8</a>, E2P form with <a href="/xray-mp-wiki/reagents/ligands/bufalin/">Bufalin</a> in presence of K+</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM MES (titrated with NMDG, pH 6.2) with ~150 mM K+</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>19</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Additional 80% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>; flash-cooled in liquid nitrogen</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>E2P-<a href="/xray-mp-wiki/reagents/ligands/bufalin/">Bufalin</a> complex. Space group P21, a=65.9, b=240.3, c=152.7 A, beta=102.3 deg, two alphabeta-gamma heterotrimers per asymmetric unit, solvent content 68%. Anisotropic data truncated to 5.6, 4.1, 3.4 A. <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> with PDB 4HYT. Rwork/Rfree=24.5/28.8%. Data collected at Swiss Light Source X06SA at 100 K. Unique crystal form only obtained with K+ present.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4res">4RES</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKGVGRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTPEWVKF</span><span class="topo-membrane">CRQLFGGFSMLLWIGAILCFLAYGIQ</span><span class="topo-inside">AATE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EEP</span><span class="topo-membrane">QNDNLYLGVVLSAVVIITGCFS</span><span class="topo-outside">YYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AFFSTNCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHF</span><span class="topo-membrane">IHIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLATVTV</span><span class="topo-outside">CLTLTAKRMARKNCLVKNLE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AVETLGSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPF</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">NSTNKYQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">VGKCRSAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">PASKKADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKK</span><span class="topo-membrane">SIAYTLTSNIPEITPFLIFIIA</span><span class="topo-inside">NIPL</span><span class="topo-membrane">PLGTVTILCIDLGTDMVPAISL</span><span class="topo-outside">AYEQAESDIMKRQPRNPKTD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">KLVNE</span><span class="topo-membrane">QLISMAYGQIGMIQALGGFFTYFV</span><span class="topo-inside">ILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTC</span><span class="topo-membrane">HTPFFVTIVVVQWADLVICK</span><span class="topo-outside">TRRNSVFQQGMKNK</span><span class="topo-membrane">ILIFGLFEET</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020 </span>
<span class="topo-line"><span class="topo-membrane">ALAAFLSYCP</span><span class="topo-inside">GMGVALRMYP</span><span class="topo-membrane">LKPTWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>25</td>
      <td>-4</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>90</td>
      <td>21</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>116</td>
      <td>86</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>123</td>
      <td>112</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>145</td>
      <td>119</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>289</td>
      <td>141</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>285</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>315</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>340</td>
      <td>311</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>772</td>
      <td>336</td>
      <td>767</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>773</td>
      <td>794</td>
      <td>768</td>
      <td>789</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>795</td>
      <td>798</td>
      <td>790</td>
      <td>793</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>799</td>
      <td>820</td>
      <td>794</td>
      <td>815</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>821</td>
      <td>845</td>
      <td>816</td>
      <td>840</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>846</td>
      <td>869</td>
      <td>841</td>
      <td>864</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>870</td>
      <td>916</td>
      <td>865</td>
      <td>911</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>917</td>
      <td>936</td>
      <td>912</td>
      <td>931</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>937</td>
      <td>950</td>
      <td>932</td>
      <td>945</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>951</td>
      <td>970</td>
      <td>946</td>
      <td>965</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>971</td>
      <td>980</td>
      <td>966</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>981</td>
      <td>1003</td>
      <td>976</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1021</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4res">4RES</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSWKKF</span><span class="topo-outside">IWNSEKKEFLGRTGGSW</span><span class="topo-membrane">FKILLFYVIFYGCLAGIFIGTIQVM</span><span class="topo-inside">LLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>16</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>57</td>
      <td>33</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>303</td>
      <td>58</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4res">4RES</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETV</span><span class="topo-membrane">RNGGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>26</td>
      <td>17</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>46</td>
      <td>27</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4res">4RES</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKGVGRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTPEWVKF</span><span class="topo-membrane">CRQLFGGFSMLLWIGAILCFLAYGIQ</span><span class="topo-inside">AATE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">EEP</span><span class="topo-membrane">QNDNLYLGVVLSAVVIITGCFS</span><span class="topo-outside">YYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">AFFSTNCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHF</span><span class="topo-membrane">IHIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLATVTV</span><span class="topo-outside">CLTLTAKRMARKNCLVKNLE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">AVETLGSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPF</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">NSTNKYQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">VGKCRSAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">PASKKADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKK</span><span class="topo-membrane">SIAYTLTSNIPEITPFLIFIIA</span><span class="topo-inside">NIPL</span><span class="topo-membrane">PLGTVTILCIDLGTDMVPAISL</span><span class="topo-outside">AYEQAESDIMKRQPRNPKTD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">KLVNE</span><span class="topo-membrane">QLISMAYGQIGMIQALGGFFTYFV</span><span class="topo-inside">ILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTC</span><span class="topo-membrane">HTPFFVTIVVVQWADLVICK</span><span class="topo-outside">TRRNSVFQQGMKNK</span><span class="topo-membrane">ILIFGLFEET</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020 </span>
<span class="topo-line"><span class="topo-membrane">ALAAFLSYCP</span><span class="topo-inside">GMGVALRMYP</span><span class="topo-membrane">LKPTWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>25</td>
      <td>-4</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>26</td>
      <td>90</td>
      <td>21</td>
      <td>85</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>116</td>
      <td>86</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>123</td>
      <td>112</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>124</td>
      <td>145</td>
      <td>119</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>289</td>
      <td>141</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>311</td>
      <td>285</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>315</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>340</td>
      <td>311</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>772</td>
      <td>336</td>
      <td>767</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>773</td>
      <td>794</td>
      <td>768</td>
      <td>789</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>795</td>
      <td>798</td>
      <td>790</td>
      <td>793</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>799</td>
      <td>820</td>
      <td>794</td>
      <td>815</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>821</td>
      <td>845</td>
      <td>816</td>
      <td>840</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>846</td>
      <td>869</td>
      <td>841</td>
      <td>864</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>870</td>
      <td>916</td>
      <td>865</td>
      <td>911</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>917</td>
      <td>936</td>
      <td>912</td>
      <td>931</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>937</td>
      <td>950</td>
      <td>932</td>
      <td>945</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>951</td>
      <td>970</td>
      <td>946</td>
      <td>965</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>971</td>
      <td>980</td>
      <td>966</td>
      <td>975</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>981</td>
      <td>1003</td>
      <td>976</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1021</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4res">4RES</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSWKKF</span><span class="topo-outside">IWNSEKKEFLGRTGGSW</span><span class="topo-membrane">FKILLFYVIFYGCLAGIFIGTIQVM</span><span class="topo-inside">LLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>15</td>
      <td>1</td>
      <td>15</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>16</td>
      <td>32</td>
      <td>16</td>
      <td>32</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>57</td>
      <td>33</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>303</td>
      <td>58</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4res">4RES</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETV</span><span class="topo-membrane">RNGGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
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
      <td>16</td>
      <td>1</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>17</td>
      <td>26</td>
      <td>17</td>
      <td>26</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>27</td>
      <td>46</td>
      <td>27</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1126##science.1243352 (1 structure, 3 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4hqj">4HQJ</a></td>
      <td>4.3</td>
      <td>not specified</td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma (FXYD2) subunits in [Na3]E1-AlF4--ADP state</td>
      <td>Na+ (3 ions, sites I, II, IIIb), AlF4-, ADP</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pig (Sus scrofa) kidney cortex, native extraction
- **Construct**: Native Na+,K+-ATPase from pig kidney outer medulla; no heterologous expression tags or mutations

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hqj">4HQJ</a> — Chain C (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGKGVGRDKYEPAAVSEHGDKKKAKKERDMDELK</span><span class="topo-inside">KEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTPE</span><span class="topo-membrane">WVKFCRQLFGGFSMLLWIGAILCFLAY</span><span class="topo-outside">GIQAATE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EEPQNDN</span><span class="topo-membrane">LYLGVVLSAVVIITGCFSYYQE</span><span class="topo-inside">AKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNI</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">AFFSTNCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIE</span><span class="topo-membrane">HFIHIITGVAVFLGVSFFILSLI</span><span class="topo-outside">LEYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLATVTV</span><span class="topo-inside">CLTLTAKRMARKNCLVKNLE</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">AVETLGSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPF</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">NSTNKYQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">VGKCRSAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">PASKKADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNL</span><span class="topo-membrane">KKSIAYTLTSNIPEITPFLIFIIA</span><span class="topo-outside">NIPL</span><span class="topo-membrane">PLGTVTILCIDLGTDMVPAISLAYE</span><span class="topo-inside">QAESDIMKRQPRNPKTD</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">KLV</span><span class="topo-membrane">NEQLISMAYGQIGMIQALGGFFTYFV</span><span class="topo-outside">ILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTC</span><span class="topo-membrane">HTPFFVTIVVVQWADLVICKT</span><span class="topo-inside">RRNSVFQQG</span><span class="topo-membrane">MKNKILIFGLFEET</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020 </span>
<span class="topo-line"><span class="topo-membrane">ALAAFLSYC</span><span class="topo-outside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVRKL</span><span class="topo-inside">IIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (22 regions)</summary>
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
      <td>34</td>
      <td>-4</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>35</td>
      <td>86</td>
      <td>30</td>
      <td>81</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>113</td>
      <td>82</td>
      <td>108</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>114</td>
      <td>127</td>
      <td>109</td>
      <td>122</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>128</td>
      <td>149</td>
      <td>123</td>
      <td>144</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>150</td>
      <td>287</td>
      <td>145</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>310</td>
      <td>283</td>
      <td>305</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>315</td>
      <td>306</td>
      <td>310</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>316</td>
      <td>340</td>
      <td>311</td>
      <td>335</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>341</td>
      <td>770</td>
      <td>336</td>
      <td>765</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>771</td>
      <td>794</td>
      <td>766</td>
      <td>789</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>795</td>
      <td>798</td>
      <td>790</td>
      <td>793</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>799</td>
      <td>823</td>
      <td>794</td>
      <td>818</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>824</td>
      <td>843</td>
      <td>819</td>
      <td>838</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>844</td>
      <td>869</td>
      <td>839</td>
      <td>864</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>870</td>
      <td>916</td>
      <td>865</td>
      <td>911</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>917</td>
      <td>937</td>
      <td>912</td>
      <td>932</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>938</td>
      <td>946</td>
      <td>933</td>
      <td>941</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>969</td>
      <td>942</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>970</td>
      <td>983</td>
      <td>965</td>
      <td>978</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>984</td>
      <td>1005</td>
      <td>979</td>
      <td>1000</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1006</td>
      <td>1021</td>
      <td>1001</td>
      <td>1016</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hqj">4HQJ</a> — Chain D (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSWKKFIWN</span><span class="topo-inside">SEKKEFLGRTGGS</span><span class="topo-membrane">WFKILLFYVIFYGCLAGIFIGTIQVM</span><span class="topo-outside">LLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">MIFEDCGNVPSELKERGEYNNERGERKVCRSRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-outside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>18</td>
      <td>1</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>31</td>
      <td>19</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>32</td>
      <td>57</td>
      <td>32</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>58</td>
      <td>303</td>
      <td>58</td>
      <td>303</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4hqj">4HQJ</a> — Chain E (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDVDP</span><span class="topo-outside">FYYDYETVRNG</span><span class="topo-membrane">GLIFAALAFIVGLIILLS</span><span class="topo-unknown">KRLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (4 regions)</summary>
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
      <td>18</td>
      <td>1</td>
      <td>18</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>19</td>
      <td>29</td>
      <td>19</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>47</td>
      <td>30</td>
      <td>47</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>48</td>
      <td>65</td>
      <td>48</td>
      <td>65</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>

<details class="pub-entry" markdown="1">
<summary><strong>doi/10.1073##pnas.2020438118 (9 structures, 27 sequences)</strong></summary>

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a></td>
      <td>~3.5</td>
      <td>P2_12_12_1</td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2·BeF3-·Mg2+ (E2P ground state, free of CTS)</td>
      <td>BeF3-, Mg2+ (bound at cation site II)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a></td>
      <td>2.9</td>
      <td>P2_12_12_1</td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P^Pi·Mg2+ with bound ouabain (OBN)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a>, Mg2+ (bound at cation site II)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a></td>
      <td>~3.5</td>
      <td></td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P^Pi·Mg2+ with bound bufalin (BUF)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bufalin/">Bufalin</a>, Mg2+ (bound at cation site II)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a></td>
      <td>~3.5</td>
      <td></td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P^Pi·Mg2+ with bound digitoxin (DTX)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/digitoxin/">Digitoxin</a>, Mg2+ (bound at cation site II)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a></td>
      <td>~3.5</td>
      <td></td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P^Pi·Mg2+ with bound digoxin (DGX)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/digoxin/">Digoxin</a>, Mg2+ (bound at cation site II)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a></td>
      <td>~3.5</td>
      <td></td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P^Pi·Mg2+ with bound rostafuroxin (ROS)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/rostafuroxin/">Rostafuroxin</a>, Mg2+ (bound at cation site II)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a></td>
      <td>~3.5</td>
      <td></td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P^Pi·Mg2+ with bound istaroxime (IST)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/istaroxime/">Istaroxime</a>, Mg2+ (bound at cation site II)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a></td>
      <td>~3.6</td>
      <td>P2_12_12_1</td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P^Pi·Mg2+ with anthroylouabain (AO) (soaked into ROS cocrystals)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a> (anthroyl derivative), Mg2+ (bound at cation site II)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a></td>
      <td>~3.5</td>
      <td></td>
      <td>Pig kidney Na+,K+-ATPase alpha1, beta1, and gamma subunits in E2P^Pi·K+·Mg2+ with bound bufalin (BUF) — Rb+ soaking experiment</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bufalin/">Bufalin</a>, Rb+ (at site I), Mg2+ (at site II)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pig (Sus scrofa) kidney cortex, native extraction
- **Construct**: Native Na+,K+-ATPase from pig kidney outer medulla; no heterologous expression tags or mutations

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTP</span><span class="topo-unknown">EWVKFCRQLF</span><span class="topo-outside">GGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATEEEPQN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFST</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLEAVETL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLIFII</span><span class="topo-inside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAIS</span><span class="topo-outside">LAYEQAESDIMKRQPRNPKTDKLVNE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">QL</span><span class="topo-membrane">ISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-outside">KTRRNSVFQQGMKNKI</span><span class="topo-membrane">LIFGLFEETALAAF</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      </span>
<span class="topo-line"><span class="topo-membrane">LSYC</span><span class="topo-inside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>21</td>
      <td>80</td>
      <td>21</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>91</td>
      <td>93</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>285</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>768</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>769</td>
      <td>788</td>
      <td>769</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>789</td>
      <td>794</td>
      <td>789</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>795</td>
      <td>814</td>
      <td>795</td>
      <td>814</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>815</td>
      <td>842</td>
      <td>815</td>
      <td>842</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>843</td>
      <td>862</td>
      <td>843</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>863</td>
      <td>912</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>964</td>
      <td>947</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>965</td>
      <td>978</td>
      <td>965</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>979</td>
      <td>998</td>
      <td>979</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1016</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRN</span><span class="topo-membrane">GGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>28</td>
      <td>17</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTP</span><span class="topo-unknown">EWVKFCRQLF</span><span class="topo-outside">GGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATEEEPQN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFST</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLEAVETL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLIFII</span><span class="topo-inside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAIS</span><span class="topo-outside">LAYEQAESDIMKRQPRNPKTDKLVNE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">QL</span><span class="topo-membrane">ISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-outside">KTRRNSVFQQGMKNKI</span><span class="topo-membrane">LIFGLFEETALAAF</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      </span>
<span class="topo-line"><span class="topo-membrane">LSYC</span><span class="topo-inside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>21</td>
      <td>80</td>
      <td>21</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>91</td>
      <td>93</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>285</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>768</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>769</td>
      <td>788</td>
      <td>769</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>789</td>
      <td>794</td>
      <td>789</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>795</td>
      <td>814</td>
      <td>795</td>
      <td>814</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>815</td>
      <td>842</td>
      <td>815</td>
      <td>842</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>843</td>
      <td>862</td>
      <td>843</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>863</td>
      <td>912</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>964</td>
      <td>947</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>965</td>
      <td>978</td>
      <td>965</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>979</td>
      <td>998</td>
      <td>979</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1016</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRN</span><span class="topo-membrane">GGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>28</td>
      <td>17</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTP</span><span class="topo-unknown">EWVKFCRQLF</span><span class="topo-outside">GGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATEEEPQN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFST</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLEAVETL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLIFII</span><span class="topo-inside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAIS</span><span class="topo-outside">LAYEQAESDIMKRQPRNPKTDKLVNE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">QL</span><span class="topo-membrane">ISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-outside">KTRRNSVFQQGMKNKI</span><span class="topo-membrane">LIFGLFEETALAAF</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      </span>
<span class="topo-line"><span class="topo-membrane">LSYC</span><span class="topo-inside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>21</td>
      <td>80</td>
      <td>21</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>91</td>
      <td>93</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>285</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>768</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>769</td>
      <td>788</td>
      <td>769</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>789</td>
      <td>794</td>
      <td>789</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>795</td>
      <td>814</td>
      <td>795</td>
      <td>814</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>815</td>
      <td>842</td>
      <td>815</td>
      <td>842</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>843</td>
      <td>862</td>
      <td>843</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>863</td>
      <td>912</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>964</td>
      <td>947</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>965</td>
      <td>978</td>
      <td>965</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>979</td>
      <td>998</td>
      <td>979</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1016</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRN</span><span class="topo-membrane">GGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>28</td>
      <td>17</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTP</span><span class="topo-unknown">EWVKFCRQLF</span><span class="topo-outside">GGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATEEEPQN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFST</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLEAVETL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLIFII</span><span class="topo-inside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAIS</span><span class="topo-outside">LAYEQAESDIMKRQPRNPKTDKLVNE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">QL</span><span class="topo-membrane">ISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-outside">KTRRNSVFQQGMKNKI</span><span class="topo-membrane">LIFGLFEETALAAF</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      </span>
<span class="topo-line"><span class="topo-membrane">LSYC</span><span class="topo-inside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>21</td>
      <td>80</td>
      <td>21</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>91</td>
      <td>93</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>285</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>768</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>769</td>
      <td>788</td>
      <td>769</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>789</td>
      <td>794</td>
      <td>789</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>795</td>
      <td>814</td>
      <td>795</td>
      <td>814</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>815</td>
      <td>842</td>
      <td>815</td>
      <td>842</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>843</td>
      <td>862</td>
      <td>843</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>863</td>
      <td>912</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>964</td>
      <td>947</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>965</td>
      <td>978</td>
      <td>965</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>979</td>
      <td>998</td>
      <td>979</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1016</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRN</span><span class="topo-membrane">GGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>28</td>
      <td>17</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTP</span><span class="topo-unknown">EWVKFCRQLF</span><span class="topo-outside">GGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATEEEPQN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFST</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLEAVETL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLIFII</span><span class="topo-inside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAIS</span><span class="topo-outside">LAYEQAESDIMKRQPRNPKTDKLVNE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">QL</span><span class="topo-membrane">ISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-outside">KTRRNSVFQQGMKNKI</span><span class="topo-membrane">LIFGLFEETALAAF</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      </span>
<span class="topo-line"><span class="topo-membrane">LSYC</span><span class="topo-inside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>21</td>
      <td>80</td>
      <td>21</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>91</td>
      <td>93</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>285</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>768</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>769</td>
      <td>788</td>
      <td>769</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>789</td>
      <td>794</td>
      <td>789</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>795</td>
      <td>814</td>
      <td>795</td>
      <td>814</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>815</td>
      <td>842</td>
      <td>815</td>
      <td>842</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>843</td>
      <td>862</td>
      <td>843</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>863</td>
      <td>912</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>964</td>
      <td>947</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>965</td>
      <td>978</td>
      <td>965</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>979</td>
      <td>998</td>
      <td>979</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1016</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRN</span><span class="topo-membrane">GGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>28</td>
      <td>17</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTP</span><span class="topo-unknown">EWVKFCRQLF</span><span class="topo-outside">GGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATEEEPQN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFST</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLEAVETL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLIFII</span><span class="topo-inside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAIS</span><span class="topo-outside">LAYEQAESDIMKRQPRNPKTDKLVNE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">QL</span><span class="topo-membrane">ISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-outside">KTRRNSVFQQGMKNKI</span><span class="topo-membrane">LIFGLFEETALAAF</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      </span>
<span class="topo-line"><span class="topo-membrane">LSYC</span><span class="topo-inside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>21</td>
      <td>80</td>
      <td>21</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>91</td>
      <td>93</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>285</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>768</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>769</td>
      <td>788</td>
      <td>769</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>789</td>
      <td>794</td>
      <td>789</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>795</td>
      <td>814</td>
      <td>795</td>
      <td>814</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>815</td>
      <td>842</td>
      <td>815</td>
      <td>842</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>843</td>
      <td>862</td>
      <td>843</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>863</td>
      <td>912</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>964</td>
      <td>947</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>965</td>
      <td>978</td>
      <td>965</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>979</td>
      <td>998</td>
      <td>979</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1016</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRN</span><span class="topo-membrane">GGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>28</td>
      <td>17</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTP</span><span class="topo-unknown">EWVKFCRQLF</span><span class="topo-outside">GGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATEEEPQN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFST</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLEAVETL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLIFII</span><span class="topo-inside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAIS</span><span class="topo-outside">LAYEQAESDIMKRQPRNPKTDKLVNE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">QL</span><span class="topo-membrane">ISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-outside">KTRRNSVFQQGMKNKI</span><span class="topo-membrane">LIFGLFEETALAAF</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      </span>
<span class="topo-line"><span class="topo-membrane">LSYC</span><span class="topo-inside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>21</td>
      <td>80</td>
      <td>21</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>91</td>
      <td>93</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>285</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>768</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>769</td>
      <td>788</td>
      <td>769</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>789</td>
      <td>794</td>
      <td>789</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>795</td>
      <td>814</td>
      <td>795</td>
      <td>814</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>815</td>
      <td>842</td>
      <td>815</td>
      <td>842</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>843</td>
      <td>862</td>
      <td>843</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>863</td>
      <td>912</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>964</td>
      <td>947</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>965</td>
      <td>978</td>
      <td>965</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>979</td>
      <td>998</td>
      <td>979</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1016</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRN</span><span class="topo-membrane">GGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>28</td>
      <td>17</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTP</span><span class="topo-unknown">EWVKFCRQLF</span><span class="topo-outside">GGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATEEEPQN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFST</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLEAVETL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLIFII</span><span class="topo-inside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAIS</span><span class="topo-outside">LAYEQAESDIMKRQPRNPKTDKLVNE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">QL</span><span class="topo-membrane">ISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-outside">KTRRNSVFQQGMKNKI</span><span class="topo-membrane">LIFGLFEETALAAF</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      </span>
<span class="topo-line"><span class="topo-membrane">LSYC</span><span class="topo-inside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>21</td>
      <td>80</td>
      <td>21</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>91</td>
      <td>93</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>285</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>768</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>769</td>
      <td>788</td>
      <td>769</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>789</td>
      <td>794</td>
      <td>789</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>795</td>
      <td>814</td>
      <td>795</td>
      <td>814</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>815</td>
      <td>842</td>
      <td>815</td>
      <td>842</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>843</td>
      <td>862</td>
      <td>843</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>863</td>
      <td>912</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>964</td>
      <td>947</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>965</td>
      <td>978</td>
      <td>965</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>979</td>
      <td>998</td>
      <td>979</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1016</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRN</span><span class="topo-membrane">GGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>28</td>
      <td>17</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GRDKYEPAAVSEHGDKKKAK</span><span class="topo-outside">KERDMDELKKEVSMDDHKLSLDELHRKYGTDLSRGLTPARAAEILARDGPNALTPPPTTP</span><span class="topo-unknown">EWVKFCRQLF</span><span class="topo-outside">GGF</span><span class="topo-membrane">SMLLWIGAILCFLAYGIQA</span><span class="topo-inside">ATEEEPQN</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">DNLYLGVVLSAVVIITGC</span><span class="topo-outside">FSYYQEAKSSKIMESFKNMVPQQALVIRNGEKMSINAEEVVVGDLVEVKGGDRIPADLRIISANGCKVDNSSLTGESEPQTRSPDFTNENPLETRNIAFFST</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">NCVEGTARGIVVYTGDRTVMGRIATLASGLEGGQTPIAAEIEHFI</span><span class="topo-membrane">HIITGVAVFLGVSFFILSLIL</span><span class="topo-inside">EYTW</span><span class="topo-membrane">LEAVIFLIGIIVANVPEGLLAT</span><span class="topo-outside">VTVCLTLTAKRMARKNCLVKNLEAVETL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GSTSTICSDKTGTLTQNRMTVAHMWSDNQIHEADTTENQSGVSFDKTSATWLALSRIAGLCNRAVFQANQENLPILKRAVAGDASESALLKCIELCCGSVKEMRERYTKIVEIPFNSTNK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">YQLSIHKNPNTAEPRHLLVMKGAPERILDRCSSILIHGKEQPLDEELKDAFQNAYLELGGLGERVLGFCHLFLPDEQFPEGFQFDTDDVNFPLDNLCFVGLISMIDPPRAAVPDAVGKCR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">SAGIKVIMVTGDHPITAKAIAKGVGIISEGNETVEDIAARLNIPVSQVNPRDAKACVVHGSDLKDMTSEQLDDILKYHTEIVFARTSPQQKLIIVEGCQRQGAIVAVTGDGVNDSPASKK</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">ADIGVAMGIAGSDVSKQAADMILLDDNFASIVTGVEEGRLIFDNLKKS</span><span class="topo-membrane">IAYTLTSNIPEITPFLIFII</span><span class="topo-inside">ANIPLP</span><span class="topo-membrane">LGTVTILCIDLGTDMVPAIS</span><span class="topo-outside">LAYEQAESDIMKRQPRNPKTDKLVNE</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">QL</span><span class="topo-membrane">ISMAYGQIGMIQALGGFFTY</span><span class="topo-inside">FVILAENGFLPIHLLGLRVNWDDRWINDVEDSYGQQWTYEQRKIVEFTCH</span><span class="topo-membrane">TPFFVTIVVVQWADLVIC</span><span class="topo-outside">KTRRNSVFQQGMKNKI</span><span class="topo-membrane">LIFGLFEETALAAF</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      </span>
<span class="topo-line"><span class="topo-membrane">LSYC</span><span class="topo-inside">PGMGVALRMYPLKP</span><span class="topo-membrane">TWWFCAFPYSLLIFVYDEVR</span><span class="topo-outside">KLIIRRRPGGWVEKETYY</span></span>
<details class="topo-details"><summary>Topology coordinates (23 regions)</summary>
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
      <td>21</td>
      <td>80</td>
      <td>21</td>
      <td>80</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>90</td>
      <td>81</td>
      <td>90</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>91</td>
      <td>93</td>
      <td>91</td>
      <td>93</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>112</td>
      <td>94</td>
      <td>112</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>113</td>
      <td>120</td>
      <td>113</td>
      <td>120</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>121</td>
      <td>138</td>
      <td>121</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>285</td>
      <td>139</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>306</td>
      <td>286</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>310</td>
      <td>307</td>
      <td>310</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>311</td>
      <td>332</td>
      <td>311</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>768</td>
      <td>333</td>
      <td>768</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>769</td>
      <td>788</td>
      <td>769</td>
      <td>788</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>789</td>
      <td>794</td>
      <td>789</td>
      <td>794</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>795</td>
      <td>814</td>
      <td>795</td>
      <td>814</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>815</td>
      <td>842</td>
      <td>815</td>
      <td>842</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>843</td>
      <td>862</td>
      <td>843</td>
      <td>862</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>863</td>
      <td>912</td>
      <td>863</td>
      <td>912</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>913</td>
      <td>930</td>
      <td>913</td>
      <td>930</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>931</td>
      <td>946</td>
      <td>931</td>
      <td>946</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>947</td>
      <td>964</td>
      <td>947</td>
      <td>964</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>965</td>
      <td>978</td>
      <td>965</td>
      <td>978</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>979</td>
      <td>998</td>
      <td>979</td>
      <td>998</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>999</td>
      <td>1016</td>
      <td>999</td>
      <td>1016</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MARGKAKEEGSW</span><span class="topo-outside">KKFIWNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGT</span><span class="topo-inside">IQVMLLTISEFKPTYQDRVAPPGLTQIPQSQKTEISFRPNDPQSYESYVVSIVRFLEKYKDLAQKDD</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MIFEDCGNVPSELKERGEYNNERGERKVCRFRLEWLGNCSGLNDETYGYKDGKPCVIIKLNRVLGFKPKPPKNESLETYPVMKYNPYVLPVHCTGKRDEDKEKVGTMEYFGLGGYPGFPL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300   </span>
<span class="topo-line"><span class="topo-inside">QYYPYYGKLLQPKYLQPLMAVQFTNLTMDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>13</td>
      <td>29</td>
      <td>13</td>
      <td>29</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>30</td>
      <td>53</td>
      <td>30</td>
      <td>53</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>54</td>
      <td>303</td>
      <td>54</td>
      <td>303</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7d91">7D91</a> — Chain G (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60     </span>
<span class="topo-line"><span class="topo-unknown">MAGLSTDDGGSPKGDV</span><span class="topo-inside">DPFYYDYETVRN</span><span class="topo-membrane">GGLIFAALAFIVGLIIIL</span><span class="topo-outside">SK</span><span class="topo-unknown">RLRCGGKKHRPINEDEL</span></span>
<details class="topo-details"><summary>Topology coordinates (3 regions)</summary>
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
      <td>17</td>
      <td>28</td>
      <td>17</td>
      <td>28</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>29</td>
      <td>46</td>
      <td>29</td>
      <td>46</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>47</td>
      <td>48</td>
      <td>47</td>
      <td>48</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
</details>


## Biological / Functional Insights

### First structure of Na+,K+-ATPase alpha-beta-gamma complex

The 2007 crystal structure of pig kidney Na+,K+-ATPase (PDB 3B8E) was the first atomic-resolution view of the sodium-potassium pump. The alpha subunit consists of 10 transmembrane helices (M1-M10) and three cytoplasmic domains: the A (actuator) domain, N (nucleotide-binding) domain, and P (phosphorylation) domain.

### High affinity ouabain binding requires E2P conformation

The E2P:[Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) complex represents a type II high affinity complex. [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) binds to a site formed at transmembrane segments alphaM1-alphaM6, plugging the ion pathway from the extracellular side.

### A domain rotation and alphaM1-2 movement enable high affinity binding

The A domain has rotated in response to phosphorylation and alphaM1-2 move towards the [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) molecule, providing for high affinity interactions and closing the ion pathway from the extracellular side.

### Phosphorylation site structure

Phosphate is covalently bound to Asp369 in the P domain as an aspartyl phosphoanhydride group, with a stabilizing Mg2+ ion.

### Mg2+ bound at cation site II in high-affinity ouabain complex

The 3.4 A structure of the [Mg]E2P-[Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) complex revealed a strong peak (7.3 sigma) in the Fo-Fc difference Fourier map representing a bound Mg2+ at cation site II. [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) binding involves an extensive hydrogen bonding network between the beta-surface hydroxyl groups of [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) and side chains of alphaM1 (Gln111, Glu117), alphaM2 (Asn122, Asp121), and alphaM6. The unsaturated five-membered lactone ring is located in a hydrophobic funnel 5 A from cation site II, allowing long-range electrostatic interactions with Mg2+. K+ binding at site II unwinds a turn of alphaM4, dragging residues Ile318-Val325 toward the cation site and hindering deep [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) binding.

### K+/Mg2+ competition at cation site II

Biochemical evidence supports competition between extracellular K+ and Mg2+ for binding at site II. High-affinity [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) binding to E2P in the presence of 3 mM Mg2+ alone was significantly decreased by 10 mM K+. Increasing Mg2+ to 12 mM reversed the inhibiting effect of K+. This explains the well-known antagonistic effect of K+ on cardiotonic steroid binding.

### Ouabain binding site architecture

[Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) sits deep within the transmembrane domain with its lactone ring buried and sugar moiety exposed to the extracellular cavity. The cis-trans-cis steroid core adopts a U-shaped conformation with convex beta-surface. Four hydroxyl groups on the beta-surface (OH1beta, OH5beta, OH10beta, OH14beta) form hydrogen bonds with Gln111, Glu117 (alphaM1), Asn122 (alphaM2), and Asp121 (alphaM2). The rhamnose sugar lies in a wide cavity lined by Glu116, Glu312, Arg880, and Asp884. Comparison with the low-affinity [K2]E2-MgFx-[Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) structure shows that K+ binding at site II prevents deep [Ouabain](/xray-mp-wiki/reagents/ligands/ouabain/) binding.

### CTS binding principles from structural comparison of digoxin, bufalin, and ouabain

Comparison of three E2P-CTS (cardiotonic steroid) crystal structures reveals a common mechanism: (i) an initial low-affinity complex forms by binding of the hydrophobic alpha-surface of the steroid core to bulky hydrophobic side chains of alphaM4-6; (ii) a subsequent conformational transition to a tight complex. The lactone type determines interactions with the cation-binding site: the six-membered lactone of [Bufalin](/xray-mp-wiki/reagents/ligands/bufalin/) extends ~1.5 A deeper than the five-membered lactones of cardenolides and directly coordinates K+ at site II. Glycosylation level affects binding depth and shifts the equilibrium toward the tight complex. [Bufalin](/xray-mp-wiki/reagents/ligands/bufalin/) binding does not require Mg2+ and is enhanced by K+ (Kd ~9 nM), whereas cardenolide binding is Mg2+-dependent and K+-antagonized. The wound form of alphaM4 is characteristic of the E2P state and favorable for high-affinity CTS binding.

### First structure of Na+,K+-ATPase in the Na+-bound E1P state

The 4.3 A crystal structure of pig kidney Na+,K+-ATPase in the [Na3]E1-AlF4--ADP state (Nyblom et al., Science 2013) captures the pump in the Na+-bound E1P conformation for the first time. The structure reveals the structural basis for occlusion of three Na+ ions. The A (actuator) domain undergoes a large ~110 degree rotation compared to E2 states, displacing the TGES motif involved in dephosphorylation of Asp369 by ~45 A. The N (nucleotide-binding) domain rotates ~80 degrees toward the P (phosphorylation) domain, stabilized by ADP-AlF4- at their interface. The P domain rotates ~35 degrees relative to the alphaM7-10 segment and moves together with the alphaM6-7 loop closer toward the TM region. In the TM domain, alphaM1-M2 undergoes rigid-body rotation toward alphaM9, alphaM3-M4 moves toward alphaM5-M6 and translates toward the cytoplasmic side, while alphaM5-M6 cytoplasmic ends move slightly toward the P domain. The beta and gamma subunits remain relatively unchanged compared to E2 states. This extensive domain and TM reorganization provides the structural basis for Na+ specificity of the intramembranous ion-binding sites in the E1P state.

### Identification of Na+ site IIIb in the Na+,K+-ATPase

Although Na+ cannot be directly observed at 4.3 A resolution, characteristic electron density features compatible with Na+ occupancy were observed at three sites. Sites I and II between alphaM4 and alphaM6 are equivalent to the Ca2+ sites of [SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)](/xray-mp-wiki/proteins/pumps-atpases/serca1a/) and also form the two K+ sites in the [K2]E2-Pi state. Site III, specific to Na+,K+-ATPase, was localized at site IIIb between alphaM5, 7, and 8 with residues Thr774, Gln854, Gln923, and Asp926. In contrast, the alternative site IIIa (adjacent, with residues Glu954, Tyr771) showed no indications of Na+ coordination. Two independent 45-ns molecular dynamics simulations yielded stable structures with Na+ bound at site IIIb. Electrophysiological leak current measurements of mutants at IIIa (Y771F, E954A) versus IIIb (D926A, D926E, Q854N) showed that IIIb mutants are less sensitive to extracellular sodium blockage of the leak, while IIIa mutations cause less leakage overall. This supports a model where Na+ binds tightly at IIIb while IIIa serves as a transient site for extracellular Na+ release and rebinding as well as mediating the proton leak current.

### E2P ground state structure reveals preformed CTS binding cavity

The crystal structure of the Na+,K+-ATPase E2·BeF3- complex (E2P ground state analog) free of cardiotonic steroids, together with eight crystal structures of seven CTSs in complex with NKA in the E2P^Pi·Mg2+ state, reveals that CTSs bind to a preformed cavity in NKA without inducing large conformational changes. The E2P ground state and all CTS-bound complexes are virtually identical (Kanai et al., PNAS 2020). This demonstrates that CTS binding in E2P^Pi·Mg2+ follows a "conformational selection" mechanism rather than induced fit. The binding cavity is wide open to the extracellular side in E2P^Pi·Mg2+ and closed in E2·MgF4^2-·2K+ due to changes in M4E helix inclination. The cavity is negatively charged (six Asp/Glu residues) and is normally used for Na+ release and K+ access during the catalytic cycle. CTSs plug into this access channel, preventing K+ binding and closure of the ion pathway.

### K+ antagonism explained by CTS lactone ring interactions with cation site II

Systematic measurements of eight CTSs under four different conditions (E2P^Pi·Mg2+, E2P^Pi·2K+, E2P^ATP, and turnover) reveal the structural basis for K+ antagonism. The K+ antagonism is severest for ouabain (13x) and digoxin (10x) but almost absent for bufalin and rostafuroxin at 100 mM K+. Rb+ soaking experiments demonstrate that site I is the first and high-affinity K+ binding site. CTS binding blocks the transition from low-affinity to high-affinity K+ binding at site II, because the completion of K+ binding is signaled by closure of the ion pathway mediated by K+ bridging at site II. The six-membered lactone of bufalin directly coordinates K+ at site II, explaining its unique K+-independent behavior.

### Isoform specificity of cardiotonic steroids explained by M1/M2 mouth size

The isoform specificity of CTSs is explained by size differences in the mouth of the binding cavity. In the alpha2 isoform, Thr114 is substituted with Met, enlarging the cavity mouth. This allows DTX/DGX (with tridigitoxose) to bind with higher affinity to alpha2, while DTN/DGN (aglycones) show the opposite preference. The path of the tridigitoxose moiety is affected by the mouth size, with constraints being more severe for DGX due to the C12 hydroxyl. These structural observations suggest a route for conferring alpha2 specificity on CTSs by modifications of the A ring of the steroid core, introducing bulky side chains with polar groups at C1 or C5 that could form hydrogen bonds with Ser119 in alpha2.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/serca1a/">SERCA1a</a> — Related P-type ATPase; structural comparison of E2-BeFx states between Na+,K+-ATPase and SERCA
- <a href="/xray-mp-wiki/proteins/pumps-atpases/shark-na-k-atpase/">Shark Na+,K+-ATPase</a> — Related Na+,K+-ATPase from different species; structural comparison
- <a href="/xray-mp-wiki/reagents/ligands/adp/">ADP (Adenosine diphosphate)</a> — ADP and ATP binding to E2-BeFx accelerates BeFx dissociation
- <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">Magnesium Chloride</a> — Essential cofactor; Mg2+ required for phosphorylation, ATPase activity, and ouabain binding
- <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8 (Octaethylene Glycol Dodecyl Ether)</a> — Detergent used for solubilization of Na+,K+-ATPase for crystallization
- <a href="/xray-mp-wiki/reagents/additives/peg/">Polyethylene Glycol (PEG)</a> — PEG 2000 MME used as crystallization precipitant
- <a href="/xray-mp-wiki/concepts/protein-families/p-type-atpase/">P-type ATPase Family</a> — Na+,K+-ATPase is a member of the P-type ATPase family
- <a href="/xray-mp-wiki/reagents/ligands/ouabain/">Ouabain</a> — Cardiotonic steroid that specifically inhibits Na+,K+-ATPase by binding with high affinity to the E2P state
- <a href="/xray-mp-wiki/reagents/ligands/digoxin/">Digoxin</a> — Trisaccharide-conjugated cardenolide CTS; E2P-digoxin complex structure at 3.9 A
- <a href="/xray-mp-wiki/reagents/ligands/bufalin/">Bufalin</a> — Nonglycosylated bufadienolide CTS; E2P-bufalin complex structure at 3.4 A
- <a href="/xray-mp-wiki/concepts/miscellaneous/cardiotonic-steroids/">Cardiotonic Steroids</a> — Na+,K+-ATPase is the primary target of cardiotonic steroids
- <a href="/xray-mp-wiki/reagents/ligands/rostafuroxin/">Rostafuroxin</a> — Novel CTS in clinical trials; E2P-ROS complex structure reveals superficial binding mode
- <a href="/xray-mp-wiki/reagents/ligands/digitoxin/">Digitoxin</a> — Cardenolide CTS with tridigitoxose; E2P-DTX complex structure at ~3.5 A
- <a href="/xray-mp-wiki/reagents/ligands/istaroxime/">Istaroxime</a> — Next-generation CTS in clinical trials; E2P-IST complex structure
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/phosphoenzyme-e2p-state/">Phosphoenzyme E2P State</a> — E2·BeF3- structure provides the E2P ground state model for understanding CTS binding
