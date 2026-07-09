---
title: "Non-Gastric H+/K+-ATPase (ngHKA)"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41467-022-32793-0]
verified: regex
uniprot_id: ['P07340', 'P54708']
---

# Non-Gastric H+/K+-ATPase (ngHKA)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span> <span class="expr-badge expr-hek293">HEK293</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P07340">UniProt: P07340</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P54708">UniProt: P54708</a>

<span class="expr-badge">Rattus norvegicus</span>

## Overview

The non-gastric H+/K+-ATPase (ngHKA, [ATP](/xray-mp-wiki/reagents/ligands/atp)12A) is a P-type 2C ATPase that participates in K+ reabsorption by the colon and kidney and contributes to acidification of the airways, a process promoting chronic respiratory infections in cystic fibrosis. This paper presents the first crystal structure of ngHKA in the K+-occluded E2-Pi state at 3.3 A resolution, revealing mechanistic differences between ngHKA and the gastric proton pump (gHKA). The structure shows that ngHKA exchanges 1 H+ and 1 K+ per cycle in an electroneutral fashion. The paper also demonstrates that four simultaneous residue substitutions (Ser794, Trp943, Cys949, Ala797Pro - SPWC mutant) convert ngHKA into a bona fide Na+/K+ pump with 3Na+:2K+ stoichiometry.


## Publications

### doi/10.1038##s41467-022-32793-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7x20">7X20</a></td>
      <td>3.3</td>
      <td>Not specified</td>
      <td>Rat ngHKA alpha subunit co-expressed with rat NKA beta1 subunit in HEK293S GnT1 cells; Asp315Gly correction applied</td>
      <td>K+ (<a href="/xray-mp-wiki/reagents/ligands/alf4">ALF4</a>- inhibited, K+-occluded E2-Pi state)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: HEK293S GnT1 cells (baculovirus-mediated transduction, BacMam)
- **Construct**: Rat ngHKA alpha subunit with N-terminal His6-EGFP-TEV tag; rat NKA beta1 subunit with N-terminal Flag-TEV tag; Asp315Gly correction applied
- **Induction**: Baculovirus transduction of mammalian cells

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>5 mg/mL purified, lipidated protein</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>10% <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a>, 33% <a href="/xray-mp-wiki/reagents/additives/peg300">PEG300</a>, 50 mM <a href="/xray-mp-wiki/reagents/buffers/glycine">Glycine</a>-NaOH pH 9.5, 100 mM NaCl, 200 mM KCl, 0.1 mM AlCl3, 0.4 mM NaF</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals flash-frozen in liquid nitrogen; RbCl substituted KCl for anomalous diffraction experiments</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7x20">7X20</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">GMDLDDHRLSNTELEQKYGTNIIQGLSSVRATELLARDGPNTLTPPKQTPE</span><span class="topo-membrane">IIKFLKQMVGGFSILLWIGAALCWIAF</span><span class="topo-outside">VIQYVNNSASLD</span><span class="topo-membrane">NVYLGAILVLVVILTGIFAYY</span><span class="topo-inside">QEAKSTNIM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">ASFSKMIPQQALVIRDAEKKVISAEQLVVGDVVEIKGGDQIPADIRLVFSQGCKVDNSSLTGESEPQARSTEFTHENPLETKNIGFYSTTCLEGTATGIVINTGDRTIIGRIASLASGVG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKTPIAIEI</span><span class="topo-membrane">EHFVHIVAGVAVSIGIIFFITAVC</span><span class="topo-outside">MKYYV</span><span class="topo-membrane">LDAIIFLISIIVANVPEGLLATVTVT</span><span class="topo-inside">LSLTAKRMAKKNCLVKNLEAVETLGSTSIICSDKTGTLTQNRMTVAHLWFDNQIF</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VADTSENQTKQAFDQSSGTWASLSKIITLCNRAEFRPGQESVPIMKRTVVGDASETALLKFSEVILGDVMGIRKRNHKVAEIPFNSTNKFQLSIHETEDPNNKRFLVVMKGAPERILEKC</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">STIMINGQEQPLDKSSADSFHTAYMELGGLGERVLGFCHLYLPAEQFPQSYIFDVDSVNFPTSNFCFVGLLSMIDPPRSTVPDAVSKCRSAGIKVIMVTGDHPITAKAIAKSVGIISANN</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">ETVEDIAKRRNIAVEQVNKREAKAAVVTGMELKDMTPEQLDELLTNYQEIVFARTSPQQKLIIVEGCQRQDAIVAVTGDGVNDSPALKKADIGIAMGIAGSDAAKNAADMVLLDDNFASI</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">VTGVEEGRLIFDNL</span><span class="topo-membrane">KKTIAYTLTKNIAELCPFLIYIV</span><span class="topo-outside">AGLPL</span><span class="topo-membrane">PIGTITILFIDLGTDIIPSIALA</span><span class="topo-inside">YEKAESDIMNRKPRHKKKDRLV</span><span class="topo-membrane">NTQLAIYSYLHIGLMQALGGFLVY</span><span class="topo-outside">FTVYAQQGF</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">WPTSLINLRVAWETDDINDLEDSYGQEWTRYQRKYLEWTGS</span><span class="topo-membrane">TAFFVAIMIQQIADLIIRKTR</span><span class="topo-inside">RNSIFQQG</span><span class="topo-membrane">LFRNKVIWVGIASQVIVALILSYGLGS</span><span class="topo-outside">VPALSFTMLRV</span><span class="topo-membrane">QYWFVAVPHAIL</span></span>
<span class="topo-ruler">       970       980      </span>
<span class="topo-line"><span class="topo-membrane">IWVYDEMRKLF</span><span class="topo-inside">IRLYPGSWWDKNMY</span><span class="topo-unknown">Y</span></span>
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
      <td>51</td>
      <td>51</td>
      <td>101</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>78</td>
      <td>102</td>
      <td>128</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>79</td>
      <td>90</td>
      <td>129</td>
      <td>140</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>91</td>
      <td>111</td>
      <td>141</td>
      <td>161</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>250</td>
      <td>162</td>
      <td>300</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>274</td>
      <td>301</td>
      <td>324</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>279</td>
      <td>325</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>280</td>
      <td>305</td>
      <td>330</td>
      <td>355</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>306</td>
      <td>734</td>
      <td>356</td>
      <td>784</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>735</td>
      <td>757</td>
      <td>785</td>
      <td>807</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>758</td>
      <td>762</td>
      <td>808</td>
      <td>812</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>763</td>
      <td>785</td>
      <td>813</td>
      <td>835</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>786</td>
      <td>807</td>
      <td>836</td>
      <td>857</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>808</td>
      <td>831</td>
      <td>858</td>
      <td>881</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>832</td>
      <td>881</td>
      <td>882</td>
      <td>931</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>882</td>
      <td>902</td>
      <td>932</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>903</td>
      <td>910</td>
      <td>953</td>
      <td>960</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>911</td>
      <td>937</td>
      <td>961</td>
      <td>987</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>938</td>
      <td>948</td>
      <td>988</td>
      <td>998</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>949</td>
      <td>971</td>
      <td>999</td>
      <td>1021</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>972</td>
      <td>985</td>
      <td>1022</td>
      <td>1035</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>986</td>
      <td>986</td>
      <td>1036</td>
      <td>1036</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7x20">7X20</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MGDYKDDDDKSSGENLYFQGMARGKAKEEGSWKKFI</span><span class="topo-inside">WNSEKKEFLGRTG</span><span class="topo-membrane">GSWFKILLFYVIFYGCLAGIFIGTIQVM</span><span class="topo-outside">LLTISELKPTYQDRVAPPGLTQIPQIQKTEISFRPNDPKSYEA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">YVLNIIRFLEKYKDSAQKDDMIFEDCGSMPSEPKERGEFNHERGERKVCRFKLDWLGNCSGLNDESYGYKEGKPCIIIKLNRVLGFKPKPPKNESLETYPLTMKYNPNVLPVQCTGKRDE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320    </span>
<span class="topo-line"><span class="topo-outside">DKDKVGNIEYFGMGGFYGFPLQYYPYYGKLLQPKYLQPLLAVQFTNLTLDTEIRIECKAYGENIGYSEKDRFQGRFDVKIEVKS</span></span>
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
      <td>36</td>
      <td>-19</td>
      <td>16</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>37</td>
      <td>49</td>
      <td>17</td>
      <td>29</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>50</td>
      <td>77</td>
      <td>30</td>
      <td>57</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>78</td>
      <td>324</td>
      <td>58</td>
      <td>304</td>
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

### Electroneutral 1H+:1K+ exchange mechanism

The ngHKA structure reveals a single K+ occluded at a site overlapping with NKA's site II, coordinated by Glu346, Asn795, Glu798, Asp823 and main-chain oxygens from Val341, Ala342, and Val344. Unlike the gastric HKA which has Glu936 on TM8 that interacts with Lys791, ngHKA has Met939, and Asp827 forms a salt bridge with Lys794, explaining the distinct cation-binding-site structure and evolved function for K+ reabsorption rather than building H+ gradients.

### Ion selectivity switching via four mutations

The SPWC quadruple mutant (Lys794Ser, Ile943Trp, Arg949Cys, Ala797Pro) converts the electroneutral ngHKA into a bona fide Na+/K+ pump with 3Na+:2K+ stoichiometry. The mutations create a third Na+-binding site (site III) and enable the concerted mechanism leading to Na+/K+ pump phosphorylation, providing a prototype for studying ion-selectivity evolution in P-type ATPases.


## Cross-References

- <a href="/xray-mp-wiki/reagents/buffers/glycine">Glycine</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/methods/structure-determination/cryo-em">Cryo-Electron Microscopy</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/ligands/atp">ATP</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/peg300">PEG300</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/protein-tags/nanobody">Nanobody</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/mgcl2">MGCL2</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/detergents/c12e8">C12E8</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/ligands/alf4">ALF4</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/dtt">DTT</a> — Entity mentioned in text
- <a href="/xray-mp-wiki/reagents/additives/glycerol">Glycerol</a> — Entity mentioned in text
