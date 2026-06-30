---
title: "Phospholamban (PLB)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [membrane-protein, xray-crystallography, pump]
sources: [doi/10.1074##jbc.M113.501585, doi/10.1038##nature11900]
verified: false
---

# Phospholamban (PLB)

## Overview

Phospholamban (PLB, also known as PLN) is a small (~52 amino acid) membrane protein that regulates the sarcoplasmic reticulum Ca2+-ATPase (SERCA) by binding to it and lowering its apparent Ca2+ affinity. PLB is primarily expressed in heart muscle in humans, whereas [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/) ([SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/)) predominates in skeletal muscle. PLB and [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/) are homologous regulators that bind SERCA in a similar fashion. Phosphorylation of PLB by protein kinase A or CaMKII relieves its inhibitory effect on SERCA, providing a key mechanism for beta-adrenergic regulation of cardiac contractility.


## Publications

### doi/10.1074##jbc.M113.501585

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4kyt">4KYT</a></td>
      <td>2.83</td>
      <td>P2_1_2_1_2_1</td>
      <td>PLB4 (superinhibitory mutant N27A, L37A, I40A, L51A) bound to <a href="/xray-mp-wiki/proteins/pumps-atpases/serca1a/">SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)</a>; E2-PLB state</td>
      <td>None (Ca2+-free)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4y3u">4Y3U</a></td>
      <td>3.51</td>
      <td>P2_1_2_1_2_1</td>
      <td>Wild-type PLB bound to <a href="/xray-mp-wiki/proteins/pumps-atpases/serca1a/">SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase)</a></td>
      <td>None (Ca2+-free)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Mammalian heart muscle, native expression
- **Construct**: Native PLB from cardiac sarcoplasmic reticulum; no heterologous expression

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
      <td>PLB expression and purification</td>
      <td>Anti-PLB monoclonal antibody (2D12) <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Anti-PLB 2D12 antibody affinity column</td>
      <td>20 mM MOPS (pH 7.2), 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.1% decyl maltoside or 0.01% dodecyl maltoside</td>
      <td>WT-PLB and PLB4 expressed in Sf21 insect cells. Eluted PLB concentrated 100-fold with Amicon concentrator, then dialyzed against buffer with detergent.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Vapor diffusion (hanging drop) via co-crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>SERCA solubilized in 2% nonyl maltoside with 0.14 mg PLB4/mg SERCA; final buffer: 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 100 mM MOPS pH 7.0, 80 mM KCl, 3 mM MgCl2, 2.8 mM <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM HEPES pH 7.0, 800 mM NaH2PO4/K2HPO4, 0.1% decyl maltoside, 100 mM NaCl, 1 mM <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA</a>, 20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>Several days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Novel alkyl mannoside detergent system. Crystals in space group P2_1_2_1_2_1. Diffraction data to 2.83 A.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4kyt">4KYT</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MEAAHSKSTEECLAYFGVSETTGLTPDQVKRHLEKYGHNELPAEE</span><span class="topo-unknown">GK</span><span class="topo-outside">SLWELVIEQFED</span><span class="topo-membrane">LLVRILLLAACISF</span><span class="topo-inside">VLAWFE</span><span class="topo-unknown">EGEETI</span><span class="topo-inside">TAFV</span><span class="topo-membrane">EPFVILLILIANAI</span><span class="topo-outside">VGVWQERNAENAIEALK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EYEPEMGKVYRADRKSVQRIKARDIVPGDIVEVAVGDKVPADIRILSIKSTTLRVDQSILTGESVSVIKHTEPVPDPRAVNQDKKNMLFSGTNIAAGKALGIVATTGVSTEIGKIRDQMA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">A</span><span class="topo-unknown">TEQ</span><span class="topo-outside">DKTPLQQKLDEFGEQLSKV</span><span class="topo-membrane">ISLICVAVWLINI</span><span class="topo-inside">GHFNDP</span><span class="topo-unknown">VHGGSW</span><span class="topo-inside">IRGA</span><span class="topo-membrane">IYYFKIAVALAVAAI</span><span class="topo-outside">PEGLPAVITTCLALGTRRMAKKNAIVRSLPSVETLGCTSVICSDKTGTLTTNQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">MSVCKMFIIDKVDGDFCSLNEFSITGSTYAPEGEVLKNDKPIRSGQFDGLVELATICALCNDSSLDFNETKGVYEKVGEATETALTTLVEKMNVFNTEVRNLSKVERANACNSVIRQLMK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">KEFTLEFSRDRKSMSVYCSPAKSSRAAVGNKMFVKGAPEGVIDRCNYVRVGTTRVPMTGPVKEKILSVIKEWGTGRDTLRCLALATRDTPPKREEMVLDDSSRFMEYETDLTFVGVVGML</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DPPRKEVMGSIQLCRDAGIRVIMITGDNKGTAIAICRRIGIFGENEEVADRAYTGREFDDLPLAEQREACRRACCFARVEPSHKSKIVEYLQSYDEITAMTGDGVNDAPALKKAEIGIAM</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">GSGTAVAKTASEMVLADDNFSTIVAAVEEGRAIYNNMKQFIRYLIS</span><span class="topo-membrane">SNVGEVVCIFLTAAL</span><span class="topo-inside">GLPE</span><span class="topo-membrane">ALIPVQLLWVNLVTDGLP</span><span class="topo-outside">ATALGFNPPDLDIMDRPPRSPKEPLISGWLFFRYM</span><span class="topo-membrane">AI</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-membrane">GGYVGAATVGAA</span><span class="topo-inside">AWWFMYAEDGPGVTYHQLTHFMQCTEDHPHFEGLDCEIFEAPEPM</span><span class="topo-membrane">TMALSVLVTIEMCNA</span><span class="topo-outside">LNSLSENQSLMRMPPWVNIWLL</span><span class="topo-membrane">GSICLSMSLHFLIL</span><span class="topo-inside">YVDPLPMIFKLK</span></span>
<span class="topo-ruler">       970       980       990    </span>
<span class="topo-line"><span class="topo-inside">ALDLTQW</span><span class="topo-membrane">LMVLKISLPVIGLD</span><span class="topo-outside">EILKFIARNYL</span><span class="topo-unknown">EG</span></span>
<details class="topo-details"><summary>Topology coordinates (30 regions)</summary>
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
      <td>45</td>
      <td>1</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>47</td>
      <td>46</td>
      <td>47</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>48</td>
      <td>59</td>
      <td>48</td>
      <td>59</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>60</td>
      <td>73</td>
      <td>60</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>79</td>
      <td>74</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>85</td>
      <td>80</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>89</td>
      <td>86</td>
      <td>89</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>90</td>
      <td>103</td>
      <td>90</td>
      <td>103</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>104</td>
      <td>241</td>
      <td>104</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>244</td>
      <td>242</td>
      <td>244</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>245</td>
      <td>263</td>
      <td>245</td>
      <td>263</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>264</td>
      <td>276</td>
      <td>264</td>
      <td>276</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>277</td>
      <td>282</td>
      <td>277</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>288</td>
      <td>283</td>
      <td>288</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>289</td>
      <td>292</td>
      <td>289</td>
      <td>292</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>293</td>
      <td>307</td>
      <td>293</td>
      <td>307</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>308</td>
      <td>766</td>
      <td>308</td>
      <td>766</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>767</td>
      <td>781</td>
      <td>767</td>
      <td>781</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>782</td>
      <td>785</td>
      <td>782</td>
      <td>785</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>786</td>
      <td>803</td>
      <td>786</td>
      <td>803</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>804</td>
      <td>838</td>
      <td>804</td>
      <td>838</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>839</td>
      <td>852</td>
      <td>839</td>
      <td>852</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>853</td>
      <td>897</td>
      <td>853</td>
      <td>897</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>898</td>
      <td>912</td>
      <td>898</td>
      <td>912</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>913</td>
      <td>934</td>
      <td>913</td>
      <td>934</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>935</td>
      <td>948</td>
      <td>935</td>
      <td>948</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>949</td>
      <td>967</td>
      <td>949</td>
      <td>967</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>968</td>
      <td>981</td>
      <td>968</td>
      <td>981</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>982</td>
      <td>992</td>
      <td>982</td>
      <td>992</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>994</td>
      <td>993</td>
      <td>994</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4kyt">4KYT</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50  </span>
<span class="topo-line"><span class="topo-unknown">MDKVQYLTRSAIRRASTIEM</span><span class="topo-outside">PQQARQALQCLFIN</span><span class="topo-membrane">FCAILICLLLICII</span><span class="topo-unknown">GMLL</span></span>
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
      <td>20</td>
      <td>1</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>34</td>
      <td>21</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>48</td>
      <td>35</td>
      <td>48</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>50</td>
      <td>52</td>
      <td>50</td>
      <td>52</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y3u">4Y3U</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MEAAHSKSTEECLAYFGVSETTGLTPDQVKRHLEKYGHNELPAEE</span><span class="topo-unknown">GK</span><span class="topo-membrane">SLWELVIEQFEDLLVRIL</span><span class="topo-inside">LLAACISFVLAWF</span><span class="topo-unknown">EEGEETI</span><span class="topo-inside">TAFVEPFV</span><span class="topo-membrane">ILLILIANAIVGVW</span><span class="topo-outside">QERNAENAIEALK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EYEPEMGKVYRADRKSVQRIKARDIVPGDIVEVAVGDKVPADIRILSIKSTTLRVDQSILTGESVSVIKHTEPVPDPRAVNQDKKNMLFSGTNIAAGKALGIVATTGVSTEIGKIRDQMA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">ATE</span><span class="topo-outside">QDKTPLQQKLDEF</span><span class="topo-membrane">GEQLSKVISLICVA</span><span class="topo-inside">VWLINIGHFNDP</span><span class="topo-unknown">VHGGSWI</span><span class="topo-inside">RGAIYYFKIA</span><span class="topo-membrane">VALAVAAIPEG</span><span class="topo-outside">LPAVITTCLALGTRRMAKKNAIVRSLPSVETLGCTSVICSDKTGTLTTNQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">MSVCKMFIIDKVDGDFCSLNEFSITGSTYAPEGEVLKNDKPIRSGQFDGLVELATICALCNDSSLDFNETKGVYEKVGEATETALTTLVEKMNVFNTEVRNLSKVERANACNSVIRQLMK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">KEFTLEFSRDRKSMSVYCSPAKS</span><span class="topo-unknown">SRA</span><span class="topo-outside">AVGNKMFVKGAPEGVIDRCNYVRVGTTRVPMTGPVKEKILSVIKEWGTGRDTLRCLALATRDTPPKREEMVLDDSSRFMEYETDLTFVGVVGML</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DPPRKEVMGSIQLCRDAGIRVIMITGDNKGTAIAICRRIGIFGENEEVADRAYTGREFDDLPLAEQREACRRACCFARVEPSHKSKIVEYLQSYDEITAMTGDGVNDAPALKKAEIGIAM</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">GSGTAVAKTASEMVLADDNFSTIVAAVEEGRAIYNNMKQFIR</span><span class="topo-membrane">YLISSNVGEVVCIFL</span><span class="topo-inside">TAALGLPEALIPV</span><span class="topo-membrane">QLLWVNLVTDGLPAT</span><span class="topo-outside">ALGFNPPDLDIMDRPPRSPKEPLISGWL</span><span class="topo-membrane">FFRYMAI</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-membrane">GGYVGAATVG</span><span class="topo-inside">AAAWWFMYAEDGPGVTYHQLTHFMQCTEDHPHFEGLDCEIFEAPEPMTM</span><span class="topo-membrane">ALSVLVTIEMCNALN</span><span class="topo-outside">SLSENQSLMRMPPWVNIW</span><span class="topo-membrane">LLGSICLSMSLHFL</span><span class="topo-inside">ILYVDPLPMIFKLK</span></span>
<span class="topo-ruler">       970       980       990    </span>
<span class="topo-line"><span class="topo-inside">ALDLTQ</span><span class="topo-membrane">WLMVLKISLPVIGLD</span><span class="topo-outside">EILKFIARNYL</span><span class="topo-unknown">EG</span></span>
<details class="topo-details"><summary>Topology coordinates (31 regions)</summary>
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
      <td>45</td>
      <td>1</td>
      <td>45</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>46</td>
      <td>47</td>
      <td>46</td>
      <td>47</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>48</td>
      <td>65</td>
      <td>48</td>
      <td>65</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>66</td>
      <td>78</td>
      <td>66</td>
      <td>78</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>79</td>
      <td>85</td>
      <td>79</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>93</td>
      <td>86</td>
      <td>93</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>94</td>
      <td>107</td>
      <td>94</td>
      <td>107</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>108</td>
      <td>240</td>
      <td>108</td>
      <td>240</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>241</td>
      <td>243</td>
      <td>241</td>
      <td>243</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>244</td>
      <td>256</td>
      <td>244</td>
      <td>256</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>257</td>
      <td>270</td>
      <td>257</td>
      <td>270</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>271</td>
      <td>282</td>
      <td>271</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>283</td>
      <td>289</td>
      <td>283</td>
      <td>289</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>290</td>
      <td>299</td>
      <td>290</td>
      <td>299</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>300</td>
      <td>310</td>
      <td>300</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>503</td>
      <td>311</td>
      <td>503</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>504</td>
      <td>506</td>
      <td>504</td>
      <td>506</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>507</td>
      <td>762</td>
      <td>507</td>
      <td>762</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>763</td>
      <td>777</td>
      <td>763</td>
      <td>777</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>778</td>
      <td>790</td>
      <td>778</td>
      <td>790</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>791</td>
      <td>805</td>
      <td>791</td>
      <td>805</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>806</td>
      <td>833</td>
      <td>806</td>
      <td>833</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>834</td>
      <td>850</td>
      <td>834</td>
      <td>850</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>851</td>
      <td>899</td>
      <td>851</td>
      <td>899</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>900</td>
      <td>914</td>
      <td>900</td>
      <td>914</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>915</td>
      <td>932</td>
      <td>915</td>
      <td>932</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>933</td>
      <td>946</td>
      <td>933</td>
      <td>946</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>947</td>
      <td>966</td>
      <td>947</td>
      <td>966</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>967</td>
      <td>981</td>
      <td>967</td>
      <td>981</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>982</td>
      <td>992</td>
      <td>982</td>
      <td>992</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>993</td>
      <td>994</td>
      <td>993</td>
      <td>994</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y3u">4Y3U</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50</span>
<span class="topo-line"><span class="topo-unknown">MDKVQYLTRSAIRRASTIEM</span><span class="topo-outside">PQQARQNLQN</span><span class="topo-membrane">LFINFCLILICLLL</span><span class="topo-inside">ICIIVM</span></span>
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
      <td>20</td>
      <td>1</td>
      <td>20</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>21</td>
      <td>30</td>
      <td>21</td>
      <td>30</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>31</td>
      <td>44</td>
      <td>31</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>45</td>
      <td>50</td>
      <td>45</td>
      <td>50</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4y3u">4Y3U</a> — Chain C (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20   </span>
<span class="topo-line"><span class="topo-unknown">UUUUUUU</span><span class="topo-membrane">UUUUUUUUUUU</span><span class="topo-inside">UUUUU</span></span>
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
      <td>94</td>
      <td>100</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>8</td>
      <td>18</td>
      <td>101</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>19</td>
      <td>23</td>
      <td>112</td>
      <td>116</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1038##nature11900

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4h1w">4H1W</a></td>
      <td>Low resolution (~20 A)</td>
      <td>Not determined</td>
      <td>PLB-SERCA complex observed by electron microscopy</td>
      <td>Not determined</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Mammalian heart muscle, native expression
- **Construct**: Native PLB from cardiac sarcoplasmic reticulum; no heterologous expression

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h1w">4H1W</a> — Chain A (10 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MEAAHSKSTEECLAYFGVSETTGLTPDQVKRHLEKYGHNELPAEEG</span><span class="topo-membrane">KSLWELVIEQFEDLLVRILLLA</span><span class="topo-inside">ACISFVLAWFE</span><span class="topo-unknown">EGEETI</span><span class="topo-inside">TAFVEP</span><span class="topo-membrane">FVILLILIANAIVGVWQERN</span><span class="topo-outside">AENAIEALK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EYEPEMGKVYRADRKSVQRIKARDIVPGDIVEVAVGDKVPADIRILSIKSTTLRVDQSILTGESVSVIKHTEPVPDPRAVNQDKKNMLFSGTNIAAGKALGIVATTGVSTEIGKIRDQMA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">ATEQDKTPLQQKLD</span><span class="topo-membrane">EFGEQLSKVISLICVAVWLI</span><span class="topo-inside">NIGHFNDPVHGGSWIRGAIYYF</span><span class="topo-membrane">KIAVALAVAAIPEGLPAV</span><span class="topo-outside">ITTCLALGTRRMAKKNAIVRSLPSVETLGCTSVICSDKTGTLTTNQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">MSVCKMFIIDKVDGDFCSLNEFSITGSTYAPEGEVLKNDKPIRSGQFDGLVELATICALCNDSSLDFNETKGVYEKVGEATETALTTLVEKMNVFNTEVRNLSKVERANACNSVIRQLMK</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">KEFTLEFSRDRKSMSVYCSPAKSSRAAVGNKMFVKGAPEGVIDRCNYVRVGTTRVPMTGPVKEKILSVIKEWGTGRDTLRCLALATRDTPPKREEMVLDDSSRFMEYETDLTFVGVVGML</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">DPPRKEVMGSIQLCRDAGIRVIMITGDNKGTAIAICRRIGIFGENEEVADRAYTGREFDDLPLAEQREACRRACCFARVEPSHKSKIVEYLQSYDEITAMTGDGVNDAPALKKAEIGIAM</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">GSGTAVAKTASEMVLADDNFSTIVAAVEEGRAIYNNMKQ</span><span class="topo-membrane">FIRYLISSNVGEVVCIFLTAAL</span><span class="topo-inside">GLPEA</span><span class="topo-membrane">LIPVQLLWVNLVTDGLPATALGF</span><span class="topo-outside">NPPDLDIMDRPPRSPKEPLISGW</span><span class="topo-membrane">LFFRYMAI</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-membrane">GGYVGAATVGAAAW</span><span class="topo-inside">WFMYAEDGPGVTYHQLTHFMQCTEDHPHF</span><span class="topo-unknown">EGL</span><span class="topo-inside">DCEIFEAPEPM</span><span class="topo-membrane">TMALSVLVTIEMCNALNSL</span><span class="topo-outside">SENQSLMRMP</span><span class="topo-membrane">PWVNIWLLGSICLSMSLHFLIL</span><span class="topo-inside">YVDPLPMIFKLK</span></span>
<span class="topo-ruler">       970       980       990    </span>
<span class="topo-line"><span class="topo-inside">ALDL</span><span class="topo-membrane">TQWLMVLKISLPVIGLDEILKFI</span><span class="topo-outside">ARNYLEG</span></span>
<details class="topo-details"><summary>Topology coordinates (25 regions)</summary>
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
      <td>46</td>
      <td>1</td>
      <td>46</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>68</td>
      <td>47</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>79</td>
      <td>69</td>
      <td>79</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>80</td>
      <td>85</td>
      <td>80</td>
      <td>85</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>86</td>
      <td>91</td>
      <td>86</td>
      <td>91</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>92</td>
      <td>111</td>
      <td>92</td>
      <td>111</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>112</td>
      <td>254</td>
      <td>112</td>
      <td>254</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>255</td>
      <td>274</td>
      <td>255</td>
      <td>274</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>275</td>
      <td>296</td>
      <td>275</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>314</td>
      <td>297</td>
      <td>314</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>315</td>
      <td>759</td>
      <td>315</td>
      <td>759</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>760</td>
      <td>781</td>
      <td>760</td>
      <td>781</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>782</td>
      <td>786</td>
      <td>782</td>
      <td>786</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>787</td>
      <td>809</td>
      <td>787</td>
      <td>809</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>810</td>
      <td>832</td>
      <td>810</td>
      <td>832</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>833</td>
      <td>854</td>
      <td>833</td>
      <td>854</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>855</td>
      <td>883</td>
      <td>855</td>
      <td>883</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>884</td>
      <td>886</td>
      <td>884</td>
      <td>886</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>887</td>
      <td>897</td>
      <td>887</td>
      <td>897</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>898</td>
      <td>916</td>
      <td>898</td>
      <td>916</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>917</td>
      <td>926</td>
      <td>917</td>
      <td>926</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>927</td>
      <td>948</td>
      <td>927</td>
      <td>948</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>949</td>
      <td>964</td>
      <td>949</td>
      <td>964</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>965</td>
      <td>987</td>
      <td>965</td>
      <td>987</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>988</td>
      <td>994</td>
      <td>988</td>
      <td>994</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4h1w">4H1W</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30 </span>
<span class="topo-line"><span class="topo-outside">MER</span><span class="topo-membrane">STRELCLNFTVVLITVILI</span><span class="topo-inside">WLLVRSYQY</span></span>
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
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>22</td>
      <td>4</td>
      <td>22</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>23</td>
      <td>31</td>
      <td>23</td>
      <td>31</td>
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

### Crystal structure of PLB-SERCA complex

The 2.83 A crystal structure of PLB4-SERCA (PDB 4KYT) reveals that PLB binds as a single transmembrane alpha-helix in a groove between M2, M4, M6, M9 of SERCA. The structure stabilizes the E2-PLB conformation with collapsed Ca2+ binding sites, explaining how dephosphorylated PLB decreases Ca2+ affinity.

### Asn34 is the key inhibitory residue

Asn34 of PLB forms hydrogen bonds with Gly801 (main chain carbonyl) and Thr805 (side chain) of SERCA M6. Mutation N34A completely disables PLB inhibition. Asn34 is positioned in a particularly hydrophobic context, enhancing its functional impact.

### PLB pentamer-monomer equilibrium

The crystal structure confirms that PLB monomer binds SERCA, while pentamer is the storage form. The PLB4 mutant (N27A, L37A, I40A, L51A) shows increased monomer population leading to superinhibition. The Leu/Ile zipper has dual faces: one for pentamerization and one for SERCA inhibition.

### PLB and SLN regulate SERCA by different mechanisms

Unlike [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/), PLB decreases Ca2+ affinity without uncoupling ATP hydrolysis from Ca2+ transport. PLB dissociates from SERCA in the presence of Ca2+, whereas [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/) continues to interact with SERCA even with Ca2+ bound. The unique C-terminal tail of [SLN](/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/) (Arg27, Tyr31) is not present in PLB.

### Phosphorylation relieves PLB inhibition

Phosphorylation of PLB at Ser16 and Thr17 reverses the inhibitory effect by causing PLB to dissociate from SERCA. The E2-PLB structure provides the structural basis for understanding how cAMP-dependent phosphorylation regulates cardiac contractility.

### MD simulations reveal distinct rigid apolar and dynamic polar domains

Atomistic MD simulations of full-length PLN in a [POPC](/xray-mp-wiki/reagents/lipids/popc/) bilayer (starting from NMR model PDB 2KYV) showed that the C-terminal LxxIxxx-domain (residues 33-51) is tightly packed and very rigid (backbone RMSF 0.53 A), while the N-terminal TM sector is more dynamic (1.53 A) and becomes widely splayed, with water rushing into the bundle. This indicates that the apolar C-terminal domain plays the dominant role in pentamer stabilization, while polar N-terminal residues modulate functional dynamics rather than stability.


## Cross-References

- <a href="/xray-mp-wiki/proteins/pumps-atpases/serca1a/">SERCA1a (Sarcoplasmic Reticulum Ca2+-ATPase 1a)</a> — Primary target of PLB regulation; PLB binds and inhibits SERCA
- <a href="/xray-mp-wiki/proteins/pumps-atpases/sarcolipin/">Sarcolipin (SLN)</a> — Homologous regulator of SERCA; distinct mechanism from PLB
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/alternating-access-mechanism/">Alternating-Access Mechanism</a> — PLB modulates the alternating-access transport cycle of SERCA by stabilizing the E2 state
- <a href="/xray-mp-wiki/proteins/miscellaneous/pl5-pentamer/">PL5 Designed Pentameric Transmembrane Protein</a> — PL5 is a designed variant derived from PLN's apolar C-terminal domain; revealed the steric packing code underlying PLN assembly
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/egta/">EGTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/lipids/popc/">POPC</a> — Additive used in purification or crystallization buffers
