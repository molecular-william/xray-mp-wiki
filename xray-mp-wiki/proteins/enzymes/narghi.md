---
title: "Nitrate Reductase A (NarGHI) from Escherichia coli"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [enzyme, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nsb969, doi/10.1074##jbc.M410457200, doi/10.1021##bi049938l]
verified: regex
uniprot_id: ['P09152', 'P11349', 'P11350']
---

# Nitrate Reductase A (NarGHI) from Escherichia coli

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P09152">UniProt: P09152</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P11349">UniProt: P11349</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/P11350">UniProt: P11350</a>

<span class="expr-badge">Escherichia coli</span>

## Overview

Nitrate reductase A (NarGHI) is a membrane-bound quinol:nitrate oxidoreductase from Escherichia coli that reduces nitrate to nitrite under anaerobic conditions. The heterotrimeric enzyme (Mr 223,921) is composed of a molybdenum cofactor-containing catalytic subunit (NarG, 1246 residues), an [Fe-S] cluster-containing electron transfer subunit (NarH, 512 residues), and a heme-containing membrane anchor subunit (NarI, 225 residues). NarGHI forms part of a redox loop with formate dehydrogenase N (FdnGHI) to generate a proton-motive force, as proposed by Mitchell's chemiosmotic theory.

The crystal structure solved at 1.9 A resolution reveals eight redox centers aligned on a single chain spanning ~74.5 A, including two b-type hemes, four [4Fe-4S] clusters, one [3Fe-4S] cluster, and a Mo-bisMGD cofactor. A unique finding is the open bicyclic form of the molybdo-bis(molybdopterin guanine dinucleotide) cofactor and a novel fold of the membrane anchor subunit. EPR spectroscopic and crystallographic analysis of the FS0 [4Fe-4S] cluster in NarG revealed a novel His3Cys coordination and a high-spin (S=3/2) ground state.

The structure in complex with the inhibitor [PCP](/xray-mp-wiki/reagents/ligands/pentachlorophenol/) ([PCP](/xray-mp-wiki/reagents/ligands/pentachlorophenol/)) at 2.0 A resolution provided the first molecular characterization of a quinol binding and oxidation site (Q-site) in NarGHI. [PCP](/xray-mp-wiki/reagents/ligands/pentachlorophenol/) binds in a narrow hydrophobic cleft (cleft B) in NarI between helices II, III, and IV', in proximity to [HEME](/xray-mp-wiki/reagents/ligands/heme/) bD (edge-to-edge distance 2.8 A). A possible proton conduction pathway linked to electron transfer reactions has also been defined, providing fundamental atomic details of ubiquinol oxidation by NarGHI at the bacterial membrane.


## Publications

### doi/10.1038##nsb969

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1q16">1Q16</a></td>
      <td>1.9</td>
      <td>C2221</td>
      <td>Full-length NarGHI heterotrimer encoded by the narGHJI operon, expressed in E. coli LCB2048 from vector pVA700</td>
      <td>Mo-bisMGD, two hemes b (bP and bD), five [Fe-S] clusters (FS0-FS4)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli LCB2048 (Delta narGHJI, Delta narZYWV)
- **Construct**: Full narGHJI operon under tac promoter in vector pVA700
- **Notes**: Native and selenomethionine-substituted protein expressed

**Purification:**

- **Expression system**: E. coli LCB2048
- **Expression construct**: Full narGHJI operon

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
      <td>Membrane purification</td>
      <td>Centrifugation</td>
      <td>--</td>
      <td>100 mM MOPS, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> (pH 7.0) + <a href="/xray-mp-wiki/reagents/detergents/thesit/">THESIT</a></td>
      <td>Membrane fraction isolated after cell lysis by French pressure cell</td>
    </tr>
    <tr>
      <td>Detergent extraction</td>
      <td>Solubilization</td>
      <td>--</td>
      <td>-- + 0.7 mM <a href="/xray-mp-wiki/reagents/detergents/thesit/">THESIT</a> (polyoxyethylene 9-dodecyl ether)</td>
      <td>Detergent extraction from membranes</td>
    </tr>
    <tr>
      <td>Anion exchange chromatography</td>
      <td>DEAE-Sepharose</td>
      <td>DEAE-Sepharose</td>
      <td>pH 6.5 and pH 7.5 + 0.7 mM <a href="/xray-mp-wiki/reagents/detergents/thesit/">THESIT</a></td>
      <td>Two sequential anion exchange steps at different pH</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>SEC (<a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a></td>
      <td>-- + 0.7 mM <a href="/xray-mp-wiki/reagents/detergents/thesit/">THESIT</a></td>
      <td>Used to determine optimal detergent concentration for crystallization</td>
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
      <td>Purified NarGHI in 0.7 mM <a href="/xray-mp-wiki/reagents/detergents/thesit/">THESIT</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM HEPES pH 7.0, 20% (w/v) <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a>, 200 mM <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a>, 200 mM KCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>--</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Crystals soaked in reservoir solution with 35% <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a></td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals belong to space group C2221 with unit cell dimensions a=154.175 A, b=241.376 A, c=139.494 A, one complex per asymmetric unit. Native and selenomethionine-substituted crystals grown under same conditions. Structure determined by MAD near Fe K-edge and <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a>. Data collected at SSRL beamline 9-2 and NSLS X25 at 100 K.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1q16">1Q16</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGVNCTGSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MWREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAAD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LVDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">NYGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQ</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">RPARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">SGKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVG</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">HLGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLA</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">PETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSN</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">GNQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240       </span>
<span class="topo-line"><span class="topo-inside">GYAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQES</span><span class="topo-unknown">VK</span></span>
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
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>9</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>1245</td>
      <td>9</td>
      <td>1244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1246</td>
      <td>1247</td>
      <td>1245</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1q16">1Q16</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTCKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKTE</span><span class="topo-unknown">PHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>509</td>
      <td>88</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>512</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1q16">1Q16</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLTP</span><span class="topo-outside">HWM</span><span class="topo-unknown">Y</span><span class="topo-outside">EAWLPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>73</td>
      <td>48</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>76</td>
      <td>74</td>
      <td>76</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>86</td>
      <td>78</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1q16">1Q16</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGVNCTGSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMK</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">MWREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPE</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAAD</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">LVDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLA</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">NYGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQ</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">RPARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">SGKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVG</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">HLGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLA</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">PETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSN</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">GNQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240       </span>
<span class="topo-line"><span class="topo-inside">GYAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQES</span><span class="topo-unknown">VK</span></span>
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
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>9</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>10</td>
      <td>1245</td>
      <td>9</td>
      <td>1244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1246</td>
      <td>1247</td>
      <td>1245</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1q16">1Q16</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTCKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKTE</span><span class="topo-unknown">PHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>509</td>
      <td>88</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>512</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1q16">1Q16</a> — Chain F (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLTP</span><span class="topo-outside">HWM</span><span class="topo-unknown">Y</span><span class="topo-outside">EAWLPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (15 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>73</td>
      <td>48</td>
      <td>73</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>74</td>
      <td>76</td>
      <td>74</td>
      <td>76</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>78</td>
      <td>86</td>
      <td>78</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1074##jbc.M410457200

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a></td>
      <td>2.0</td>
      <td></td>
      <td>Wild-type NarGHI complex with <a href="/xray-mp-wiki/reagents/ligands/pentachlorophenol/">PCP</a> (<a href="/xray-mp-wiki/reagents/ligands/pentachlorophenol/">PCP</a>) inhibitor</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/pentachlorophenol/">PCP</a> (<a href="/xray-mp-wiki/reagents/ligands/pentachlorophenol/">PCP</a>), two hemes b (bP and bD)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a></td>
      <td>1.9</td>
      <td></td>
      <td>NarI-K86A mutant</td>
      <td>Two hemes b</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a></td>
      <td>2.5</td>
      <td></td>
      <td>NarI-H66Y mutant</td>
      <td>Two hemes b</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli LCB2048 (Delta narGHJI, Delta narZYWV)
- **Construct**: Full narGHJI operon under tac promoter in vector pVA700
- **Notes**: Native and selenomethionine-substituted protein expressed

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGVNCTGSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMKM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAADL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLAN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">YGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGSS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">GKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVGH</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">LGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLAP</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">ETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSNG</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">NQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIGG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240      </span>
<span class="topo-line"><span class="topo-inside">YAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQES</span><span class="topo-unknown">VK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1244</td>
      <td>9</td>
      <td>1244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1245</td>
      <td>1246</td>
      <td>1245</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTAKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKTE</span><span class="topo-unknown">PHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>509</td>
      <td>88</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>512</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLT</span><span class="topo-unknown">PHWMYEAW</span><span class="topo-outside">LPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>73</td>
      <td>80</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>86</td>
      <td>81</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGVNCTGSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMKM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAADL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLAN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">YGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGSS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">GKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVGH</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">LGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLAP</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">ETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSNG</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">NQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIGG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240      </span>
<span class="topo-line"><span class="topo-inside">YAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQES</span><span class="topo-unknown">VK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1244</td>
      <td>9</td>
      <td>1244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1245</td>
      <td>1246</td>
      <td>1245</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTAKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKTE</span><span class="topo-unknown">PHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>509</td>
      <td>88</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>512</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain F (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLT</span><span class="topo-unknown">PHWMYEAW</span><span class="topo-outside">LPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>73</td>
      <td>80</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>86</td>
      <td>81</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGVNCTGSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMKM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAADL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLAN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">YGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGSS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">GKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVGH</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">LGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLAP</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">ETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSNG</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">NQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIGG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240      </span>
<span class="topo-line"><span class="topo-inside">YAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQES</span><span class="topo-unknown">VK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1244</td>
      <td>9</td>
      <td>1244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1245</td>
      <td>1246</td>
      <td>1245</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTAKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKTE</span><span class="topo-unknown">PHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>509</td>
      <td>88</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>512</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLT</span><span class="topo-unknown">PHWMYEAW</span><span class="topo-outside">LPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>73</td>
      <td>80</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>86</td>
      <td>81</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGVNCTGSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMKM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAADL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLAN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">YGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGSS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">GKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVGH</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">LGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLAP</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">ETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSNG</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">NQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIGG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240      </span>
<span class="topo-line"><span class="topo-inside">YAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQES</span><span class="topo-unknown">VK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1244</td>
      <td>9</td>
      <td>1244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1245</td>
      <td>1246</td>
      <td>1245</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTAKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKTE</span><span class="topo-unknown">PHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>509</td>
      <td>88</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>512</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain F (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLT</span><span class="topo-unknown">PHWMYEAW</span><span class="topo-outside">LPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>73</td>
      <td>80</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>86</td>
      <td>81</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGVNCTGSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMKM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAADL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLAN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">YGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGSS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">GKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVGH</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">LGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLAP</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">ETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSNG</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">NQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIGG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240      </span>
<span class="topo-line"><span class="topo-inside">YAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQES</span><span class="topo-unknown">VK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1244</td>
      <td>9</td>
      <td>1244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1245</td>
      <td>1246</td>
      <td>1245</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTAKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKTE</span><span class="topo-unknown">PHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>509</td>
      <td>88</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>512</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLT</span><span class="topo-unknown">PHWMYEAW</span><span class="topo-outside">LPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>73</td>
      <td>80</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>86</td>
      <td>81</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGVNCTGSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMKM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAADL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLAN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">YGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGSS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">GKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVGH</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">LGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLAP</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">ETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSNG</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">NQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIGG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240      </span>
<span class="topo-line"><span class="topo-inside">YAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQES</span><span class="topo-unknown">VK</span></span>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1244</td>
      <td>9</td>
      <td>1244</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1245</td>
      <td>1246</td>
      <td>1245</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTAKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKTE</span><span class="topo-unknown">PHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>509</td>
      <td>88</td>
      <td>509</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>510</td>
      <td>512</td>
      <td>510</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1y4z">1Y4Z</a> — Chain F (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLT</span><span class="topo-unknown">PHWMYEAW</span><span class="topo-outside">LPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>80</td>
      <td>73</td>
      <td>80</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>81</td>
      <td>86</td>
      <td>81</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

</div>
### doi/10.1021##bi049938l

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/1siw">1SIW</a></td>
      <td>2.2</td>
      <td></td>
      <td>Apomolybdo-NarGHI (tungstate-substituted, Mo-bisMGD absent)</td>
      <td>FS0 [4Fe-4S] cluster (partial occupancy 0.5), no Mo-bisMGD</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli LCB2048 (Delta narGHJI, Delta narZYWV)
- **Construct**: Full narGHJI operon under tac promoter in vector pVA700
- **Notes**: Native and selenomethionine-substituted protein expressed

**Purification:**

- **Expression system**: E. coli TP1000 (mobAB mutant, deficient in Mo-bisMGD synthesis)
- **Expression construct**: Full narGHJI operon from pVA700

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
      <td>Cell culture</td>
      <td>Fermentation</td>
      <td>--</td>
      <td>100 mM MOPS, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> (pH 7.0) + --</td>
      <td>Grown in Terrific Broth with 15 mM sodium <a href="/xray-mp-wiki/reagents/ligands/tungstate/">Tungstate (WO4 2-)</a>; induction with 0.2 mM <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> at inoculation</td>
    </tr>
    <tr>
      <td>Membrane preparation</td>
      <td>French pressure cell lysis and differential centrifugation</td>
      <td>--</td>
      <td>100 mM MOPS, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> (pH 7.0) + --</td>
      <td>Crude membrane vesicles prepared as previously described</td>
    </tr>
    <tr>
      <td>Anion exchange chromatography</td>
      <td>DEAE-FF (Pharmacia)</td>
      <td>DEAE-FF</td>
      <td>50 mM Tricine, 5 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 10% (v/v) <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/thesit/">THESIT</a> (pH 8.0) + 0.05% <a href="/xray-mp-wiki/reagents/detergents/thesit/">THESIT</a></td>
      <td>Purified as described by Bertero et al. (2003) with modified buffer</td>
    </tr>
  </tbody>
</table>

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1siw">1SIW</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGV</span><span class="topo-unknown">NCT</span><span class="topo-inside">GSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMKM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAADL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLAN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">YGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGSS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">GKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVGH</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">LGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLAP</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">ETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSNG</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">NQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIGG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240      </span>
<span class="topo-line"><span class="topo-inside">YAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQE</span><span class="topo-unknown">SVK</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>51</td>
      <td>9</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>54</td>
      <td>52</td>
      <td>54</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>1243</td>
      <td>55</td>
      <td>1243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1244</td>
      <td>1246</td>
      <td>1244</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1siw">1SIW</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTCKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKT</span><span class="topo-unknown">EPHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>508</td>
      <td>88</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>512</td>
      <td>509</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1siw">1SIW</a> — Chain C (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLT</span><span class="topo-unknown">PHWMYE</span><span class="topo-outside">AWLPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>78</td>
      <td>73</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1siw">1SIW</a> — Chain D (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">S</span><span class="topo-unknown">KFLDRFR</span><span class="topo-inside">YFKQKGETFADGHGQLLNTNRDWEDGYRQRWQHDKIVRSTHGV</span><span class="topo-unknown">NCT</span><span class="topo-inside">GSCSWKIYVKNGLVTWETQQTDYPRTRPDLPNHEPRGCPRGASYSWYLYSANRLKYPMMRKRLMKM</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">WREAKALHSDPVEAWASIIEDADKAKSFKQARGRGGFVRSSWQEVNELIAASNVYTIKNYGPDRVAGFSPIPAMSMVSYASGARYLSLIGGTCLSFYDWYCDLPPASPQTWGEQTDVPES</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">ADWYNSSYIIAWGSNVPQTRTPDAHFFTEVRYKGTKTVAVTPDYAEIAKLCDLWLAPKQGTDAAMALAMGHVMLREFHLDNPSQYFTDYVRRYTDMPMLVMLEERDGYYAAGRMLRAADL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">VDALGQENNPEWKTVAFNTNGEMVAPNGSIGFRWGEKGKWNLEQRDGKTGEETELQLSLLGSQDEIAEVGFPYFGGDGTEHFNKVELENVLLHKLPVKRLQLADGSTALVTTVYDLTLAN</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-inside">YGLERGLNDVNCATSYDDVKAYTPAWAEQITGVSRSQIIRIAREFADNADKTHGRSMIIVGAGLNHWYHLDMNYRGLINMLIFCGCVGQSGGGWAHYVGQEKLRPQTGWQPLAFALDWQR</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-inside">PARHMNSTSYFYNHSSQWRYETVTAEELLSPMADKSRYTGHLIDFNVRAERMGWLPSAPQLGTNPLTIAGEAEKAGMNPVDYTVKSLKEGSIRFAAEQPENGKNHPRNLFIWRSNLLGSS</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-inside">GKGHEFMLKYLLGTEHGIQGKDLGQQGGVKPEEVDWQDNGLEGKLDLVVTLDFRLSSTCLYSDIILPTATWYEKDDMNTSDMHPFIHPLSAAVDPAWEAKSDWEIYKAIAKKFSEVCVGH</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-inside">LGKETDIVTLPIQHDSAAELAQPLDVKDWKKGECDLIPGKTAPHIMVVERDYPATYERFTSIGPLMEKIGNGGKGIAWNTQSEMDLLRKLNYTKAEGPAKGQPMLNTAIDAAEMILTLAP</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040      1050      1060      1070      1080</span>
<span class="topo-line"><span class="topo-inside">ETNGQVAVKAWAALSEFTGRDHTHLALNKEDEKIRFRDIQAQPRKIISSPTWSGLEDEHVSYNAGYTNVHELIPWRTLSGRQQLYQDHQWMRDFGESLLVYRPPIDTRSVKEVIGQKSNG</span></span>
<span class="topo-ruler">      1090      1100      1110      1120      1130      1140      1150      1160      1170      1180      1190      1200</span>
<span class="topo-line"><span class="topo-inside">NQEKALNFLTPHQKWGIHSTYSDNLLMLTLGRGGPVVWLSEADAKDLGIADNDWIEVFNSNGALTARAVVSQRVPAGMTMMYHAQERIVNLPGSEITQQRGGIHNSVTRITPKPTHMIGG</span></span>
<span class="topo-ruler">      1210      1220      1230      1240      </span>
<span class="topo-line"><span class="topo-inside">YAHLAYGFNYYGTVGSNRDEFVVVRKMKNIDWLDGEGNDQVQE</span><span class="topo-unknown">SVK</span></span>
<details class="topo-details"><summary>Topology coordinates (6 regions)</summary>
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
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>2</td>
      <td>8</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>9</td>
      <td>51</td>
      <td>9</td>
      <td>51</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>52</td>
      <td>54</td>
      <td>52</td>
      <td>54</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>55</td>
      <td>1243</td>
      <td>55</td>
      <td>1243</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1244</td>
      <td>1246</td>
      <td>1244</td>
      <td>1246</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1siw">1SIW</a> — Chain E (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MKIRSQVGMVLNLDKCIGCHTCSVTCKNVWTSREGVEYAWFNNVETKPGQGFPTDWENQEKYKGGWIRKINGKLQPRMGN</span><span class="topo-unknown">RAMLLGK</span><span class="topo-inside">IFANPHLPGIDDYYEPFDFDYQNLHTAPEGSKS</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">QPIARPRSLITGERMAKIEKGPNWEDDLGGEFDKLAKDKNFDNIQKAMYSQFENTFMMYLPRLCEHCLNPACVATCPSGAIYKREEDGIVLIDQDKCRGWRMCITGCPYKKIYFNWKSGK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">SEKCIFCYPRIEAGQPTVCSETCVGRIRYLGVLLYDADAIERAASTENEKDLYQRQLDVFLDPNDPKVIEQAIKDGIPLSVIEAAQQSPVYKMAMEWKLALPLHPEYRTLPMVWYVPPLS</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">PIQSAADAGELGSNGILPDVESLRIPVQYLANLLTAGDTKPVLRALKRMLAMRHYKRAETVDGKVDTRALEEVGLTEAQAQEMYRYLAIANYEDRFVVPSSHRELAREAFPEKNGCGFTF</span></span>
<span class="topo-ruler">       490       500       510  </span>
<span class="topo-line"><span class="topo-inside">GDGCHGSDTKFNLFNSRRIDAIDVTSKT</span><span class="topo-unknown">EPHP</span></span>
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
      <td>80</td>
      <td>1</td>
      <td>80</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>81</td>
      <td>87</td>
      <td>81</td>
      <td>87</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>88</td>
      <td>508</td>
      <td>88</td>
      <td>508</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>509</td>
      <td>512</td>
      <td>509</td>
      <td>512</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/1siw">1SIW</a> — Chain F (5 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MQFL</span><span class="topo-membrane">NMFFFDIYPYIAGAVFLIGSWLRY</span><span class="topo-inside">DYGQYTWRAASSQMLDRKG</span><span class="topo-membrane">MNLASNLFHIGILGIFVGHFFGMLT</span><span class="topo-unknown">PHWMYE</span><span class="topo-outside">AWLPIEVK</span><span class="topo-membrane">QKMAMFAGGASGVLCLIGGVLLLKRRLF</span><span class="topo-inside">S</span><span class="topo-unknown">PRVRA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220     </span>
<span class="topo-line"><span class="topo-unknown">T</span><span class="topo-inside">TTG</span><span class="topo-membrane">ADILILSLLVIQCALGLLTIP</span><span class="topo-outside">FSAQHMDGSEMMKLVGWAQSVVTFHGGASQHLDGVAF</span><span class="topo-membrane">IFRLHLVLGMTLFLLFPFSRLI</span><span class="topo-inside">HIWSVPVEYLTRKYQLVRARH</span></span>
<details class="topo-details"><summary>Topology coordinates (14 regions)</summary>
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
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>28</td>
      <td>5</td>
      <td>28</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>47</td>
      <td>29</td>
      <td>47</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>72</td>
      <td>48</td>
      <td>72</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>73</td>
      <td>78</td>
      <td>73</td>
      <td>78</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>79</td>
      <td>86</td>
      <td>79</td>
      <td>86</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>87</td>
      <td>114</td>
      <td>87</td>
      <td>114</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>121</td>
      <td>116</td>
      <td>121</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>122</td>
      <td>124</td>
      <td>122</td>
      <td>124</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>125</td>
      <td>145</td>
      <td>125</td>
      <td>145</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>146</td>
      <td>182</td>
      <td>146</td>
      <td>182</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>183</td>
      <td>204</td>
      <td>183</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>225</td>
      <td>205</td>
      <td>225</td>
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

### Redox loop mechanism for proton-motive force generation

NarGHI completes the electron transfer chain from formate to nitrate, coupling quinol oxidation to nitrate reduction via a redox loop mechanism. Two electrons from formate oxidation at the periplasmic site of FdnGHI are transferred to [Menaquinone](/xray-mp-wiki/reagents/ligands/menaquinone/), which diffuses across the membrane to NarGHI. Quinol oxidation at the periplasmic side of NarI releases protons to the periplasm, while electrons flow through the eight redox centers (hemes -> [Fe-S] clusters -> Mo-bisMGD) to reduce nitrate to nitrite in the cytoplasm. This vectorial electron transfer generates a proton-motive force across the cytoplasmic membrane.

### Unique Mo-bisMGD cofactor conformation

The structure reveals an open bicyclic form of the molybdo-bis(molybdopterin guanine dinucleotide) (Mo-bisMGD) cofactor, where one of the pterin rings adopts a dihydropterin form with a cleaved pyran ring. This bicyclic form represents the first structural evidence for the cofactor's direct involvement in the catalytic mechanism, with scission and condensation reactions of the pyran ring participating in handling protons necessary for nitrate reduction.

### Previously undetected [4Fe-4S] cluster FS0 in NarG

A novel [4Fe-4S] cluster (FS0) was identified in domain I of NarG, coordinated by one histidine (His50) and three cysteines (Cys54, Cys58, Cys93). This unusual coordination scheme places FS0 between the Mo-bisMGD and FS1 cluster of NarH (edge-to-edge distances of 7 A and 11 A), establishing a direct role in electron transfer. The H50S mutation leads to loss of enzyme activity.

### High-spin EPR characterization of the FS0 cluster

EPR spectroscopy of reduced NarGHI revealed a previously unobserved signal comprising peaks at g = 5.023 and g = 5.556 at cryogenic temperatures (<15 K). These features were assigned to a [4Fe-4S]+ cluster with an S = 3/2 high-spin ground state. Both peaks exhibit midpoint potentials of approximately -55 mV at pH 8.0 and are eliminated in apomolybdo-NarGHI.

### NarI membrane anchor structure

NarI contains five transmembrane helices with two b-type hemes (bP and bD) oriented perpendicular to the membrane surface. Each [HEME](/xray-mp-wiki/reagents/ligands/heme/) is coordinated by two conserved histidine residues (His-56 and His-205 for bP; His-66 and His-187 for bD). A strong kink at Ser201 in TM V allows shorter inter-[HEME](/xray-mp-wiki/reagents/ligands/heme/) distances (16 A center-to-center) than observed in cytochrome bc1 complexes.

### Quinol binding site (Q-site) characterization

The structure of NarGHI in complex with [PCP](/xray-mp-wiki/reagents/ligands/pentachlorophenol/) ([PCP](/xray-mp-wiki/reagents/ligands/pentachlorophenol/)) at 2.0 A resolution revealed the quinol binding and oxidation site (Q-site) in NarI. [PCP](/xray-mp-wiki/reagents/ligands/pentachlorophenol/) binds in a narrow hydrophobic cleft (cleft B) between helices II, III, and IV', with an edge-to-edge distance of only 2.8 A to [HEME](/xray-mp-wiki/reagents/ligands/heme/) bD. The binding pocket is distinct from the wider cleft A that exposes both hemes. [PCP](/xray-mp-wiki/reagents/ligands/pentachlorophenol/) exhibits mixed but primarily competitive inhibition with a Kic of 57 nM. His-66, which coordinates [HEME](/xray-mp-wiki/reagents/ligands/heme/) bD, is positioned within hydrogen-bonding distance from the hydroxyl group of [PCP](/xray-mp-wiki/reagents/ligands/pentachlorophenol/), suggesting a dual role as both [HEME](/xray-mp-wiki/reagents/ligands/heme/) ligand and quinone ligand. Mutation of Lys-86, which lines the proposed Q-site, to alanine (K86A) reduces plumbagin:nitrate oxidoreductase activity from 68 s-1 to 10 s-1 and attenuates inhibitor binding. A chain of water molecules between the propionates of [HEME](/xray-mp-wiki/reagents/ligands/heme/) bD and bulk solvent suggests a proton wire mechanism for proton release into the periplasm during quinol oxidation.


## Cross-References

- <a href="/xray-mp-wiki/concepts/structural-mechanisms/narghi-quinol-binding-site/">NarGHI Quinol Binding Site</a> — Detailed concept page for the Q-site architecture and mechanism
- <a href="/xray-mp-wiki/methods/structure-determination/miras/">MIRAS</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg3000/">PEG 3000</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/buffers/sodium-acetate/">Sodium Acetate</a> — Buffer component used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/detergents/thesit/">THESIT</a> — Detergent used in purification or crystallization
- <a href="/xray-mp-wiki/reagents/ligands/heme/">HEME</a> — Related ligand or cofactor
