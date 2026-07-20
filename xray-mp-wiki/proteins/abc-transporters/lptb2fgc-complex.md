---
title: "LptB2FGC LPS Transport Complex from Enterobacter cloacae and Vibrio cholerae"
created: 2026-06-08
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1038##s41586-019-1039-0]
verified: agent
uniprot_id: ['A0A0H3CQA2', 'A0A0H3CR83', 'A0A0H3CU18', 'A0A421IFY4', 'O30650', 'Q9KP51', 'Q9KP75', 'Q9KP76']
---

# LptB2FGC LPS Transport Complex from Enterobacter cloacae and Vibrio cholerae

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A0H3CQA2">UniProt: A0A0H3CQA2</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A0H3CR83">UniProt: A0A0H3CR83</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A0H3CU18">UniProt: A0A0H3CU18</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A0A421IFY4">UniProt: A0A421IFY4</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/O30650">UniProt: O30650</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9KP51">UniProt: Q9KP51</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9KP75">UniProt: Q9KP75</a> <a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q9KP76">UniProt: Q9KP76</a>

<span class="expr-badge">Vibrio cholerae</span>

## Overview

The LptB2FGC complex is the inner membrane component of the lipopolysaccharide (LPS) transport machinery in Gram-negative bacteria, comprising an ABC transporter (LptB2FG) and an accessory protein LptC. This complex powers the unidirectional extraction of LPS from the inner membrane and its transfer to the periplasmic bridge protein LptA, which ultimately delivers LPS to the outer membrane translocon LptDE. Crystal structures of the LptB2FGC complex from Enterobacter cloacae (3.2 A, PDB 6MIT) and Vibrio cholerae (2.85 A, PDB 6MJP) reveal that LptC inserts a single transmembrane helix between LptG TM1 and LptF TM5, breaking the pseudosymmetry of the transporter and defining a single pathway for LPS entry into the cavity. ATP binding and hydrolysis by the cytoplasmic ATPase LptB provides the energy to extract LPS from the membrane, while a gate in the beta-jellyroll domain of LptF prevents backward movement, ensuring unidirectional transport.

## Publications

### doi/10.1038##s41586-019-1039-0

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mit">6MIT</a></td>
      <td>3.2 A</td>
      <td>P212121</td>
      <td>E. cloacae LptB2FGC complex, LptC with C-terminal thrombin cleavage site and hepta-histidine tag</td>
      <td>Novobiocin (involved in crystal contacts only)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6mjp">6MJP</a></td>
      <td>2.85 A</td>
      <td>P212121</td>
      <td>V. cholerae LptB(E163Q)2FGC complex (catalytically inactive ATPase mutant), LptC with C-terminal thrombin cleavage site and hepta-histidine tag</td>
      <td>AMPPNP (non-hydrolysable ATP analog)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli C43
- **Construct**: LptB and LptFG cloned into pCDFduet; LptC with C-terminal thrombin-his7 tag in pBADHisA. Co-transformed into C43 E. coli.
- **Induction**: 200 uM [IPTG](/xray-mp-wiki/reagents/additives/iptg/) + 0.02% L-arabinose for 12 h at 30 C for E. cloacae; 20 C for V. cholerae in LB
- **Media**: M9 minimal media with trace elements, carbenicillin (50 ug/mL), spectinomycin (50 ug/mL) for E. cloacae; LB for V. cholerae

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
      <td>Emulsiflex C3 homogenizer (3x passes at 15,000 psi)</td>
      <td>—</td>
      <td>20 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 7.4, 300 mM NaCl, 0.2 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 1 mM PMSF, lysozyme (100 ug/mL), DNAse I (50 ug/mL), cOmplete protease inhibitors</td>
      <td>Debris removed by 12,000 x g spin; membranes pelleted at 100,000 x g for 1 h</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td>—</td>
      <td>20 mM Tris pH 7.4, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 5 mM MgCl2, cOmplete protease inhibitors + 1% w/v <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Supplemented with 2 mM ATP; rocked at 4 C for 2 h</td>
    </tr>
    <tr>
      <td>Ni-NTA affinity</td>
      <td><a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> agarose gravity flow</td>
      <td>—</td>
      <td>20 mM Tris pH 7.4, 300 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Washed with 20 CV of 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, then 30 CV wash buffer</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">SEC</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> Increase 10/300</td>
      <td>300 mM NaCl, 20 mM Tris pH 7.4, 5% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> + 0.025% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Supplemented with 0.5 mM THP. Tag cleaved with thrombin, then flowed through <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> to remove uncleaved protein</td>
    </tr>
    <tr>
      <td>Tag removal</td>
      <td>Thrombin cleavage</td>
      <td>—</td>
      <td></td>
      <td>Incubated overnight at 4 C with restriction grade thrombin; removed by passing through <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> with 8 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
  </tbody>
</table>
**Final sample**: 10-15 mg/mL in gel filtration buffer using 100-kDa cut-off concentrator

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>E. cloacae LptB2FGC at 14 mg/mL, supplemented with 2 mM Na-novobiocin</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>500 mM Li2SO4, 100 mM MES pH 6.5, 21% v/v <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Stepwise dehydration by increasing <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> concentration by 2% per day to 35%; crystals frozen directly from drops</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Streak-seeding improved crystal morphology. Novobiocin involved in crystal contacts only, not in a functionally significant site.</td>
    </tr>
  </tbody>
</table>
<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Sitting-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>V. cholerae LptB(E163Q)2FGC at 10 mg/mL with 2 mM AMPPNP</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>200 mM CaCl2, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.5, 40% v/v <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>1-6 weeks</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>Cryo-solution of 41% <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a>, 200 mM CaCl2, 300 mM NaCl, 100 mM <a href="/xray-mp-wiki/reagents/buffers/tris/">Tris-HCl Buffer</a> pH 8.5</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Long, fragile plate crystals. Crystals also obtained with wild-type protein and AMPPNP.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mit">6MIT</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ATLTAKNLAKAYKGRRVVEDVSLTVNSGEIVGLLGPNGAGKTTTFYMVVGIVPRDAGNIIIDDEDISLLPLHARARRGIGYLPQEASIFRRLSVFDNLMAVLQIRDDLTSEQRQDRANE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LMEEFHIEHLRDSLGQALSGGERRRVEIARALAANPKFILLDEPFAGVDPISVIDIKRIIEHLRDSGLGVLITDHNVRETLAVCERAYIVSQGNLIAHGTPQQILEDDHVKRVYLGEDFR</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-outside">L</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>2</td>
      <td>241</td>
      <td>2</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mit">6MIT</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-outside">ATLTAKNLAKAYKGRRVVEDVSLTVNSGEIVGLLGPNGAGKTTTFYMVVGIVPRDAGNIIIDDEDISLLPLHARARRGIGYLPQEASIFRRLSVFDNLMAVLQIRDDLTSEQRQDRANE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">LMEEFHIEHLRDSLGQALSGGERRRVEIARALAANPKFILLDEPFAGVDPISVIDIKRIIEHLRDSGLGVLITDHNVRETLAVCERAYIVSQGNLIAHGTPQQILEDDHVKRVYLGEDFR</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-outside">L</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>2</td>
      <td>241</td>
      <td>2</td>
      <td>241</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mit">6MIT</a> — Chain C (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MSKT</span><span class="topo-membrane">RRWVIILLSLVALILIGVNL</span><span class="topo-unknown">ADRDDTQTEVINNN</span><span class="topo-inside">DPTYKSDHSDTVVYSPEGALNYRLIAQHVEYFSDDGISWFTQPVMTTFDKDKVPTWSIKSDRAKLTNDRMLYLYGHVEVNAL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190     </span>
<span class="topo-line"><span class="topo-inside">TADSQLRKITTDNAQINLVTQDVTSQDLVTLYGTTFNSSGLRMRGNLRSKNAELIEKVRTSYEIQNKQT</span><span class="topo-unknown">QPLVPR</span></span>
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
      <td>1</td>
      <td>4</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>5</td>
      <td>24</td>
      <td>5</td>
      <td>24</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>39</td>
      <td>189</td>
      <td>39</td>
      <td>189</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mit">6MIT</a> — Chain F (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">MIIIRYLV</span><span class="topo-membrane">RETLKSQLAILFILLLIFFCQKLVKIL</span><span class="topo-inside">GAAVDGEIPTNLV</span><span class="topo-membrane">LSLLGLGIPEMAQLILPLSLFLGLLMT</span><span class="topo-outside">LGKLYTESEITVMHACGLSKAVLV</span><span class="topo-membrane">KAAMILALFTGIVAAVNVMWA</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GPMS</span><span class="topo-inside">SRHQDEVLAEAKANPGMAALAQGQFQQATDGNSVLFIESVDGSKFNDVFLAQLRTKGNARPSVVVADSGQLAQRKDGSQVVTLNKGTRFEGTAMLRDFRITDFQNYQAIIG</span><span class="topo-unknown">HQAVA</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">L</span><span class="topo-inside">DPTDTEQMD</span><span class="topo-unknown">MRTLWNT</span><span class="topo-inside">DTDRARA</span><span class="topo-membrane">EFHWRITLVFTVFMMALIVVPLS</span><span class="topo-outside">VVNPRQGR</span><span class="topo-membrane">VLSMLPAMLLYLIYFLLQTSIRS</span><span class="topo-inside">NGAKGKLD</span><span class="topo-membrane">PMVWTWFVNSLYILLALGLNL</span><span class="topo-outside">WDTVPVRRI</span><span class="topo-unknown">RARF</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">SRKGAI</span></span>
<details class="topo-details"><summary>Topology coordinates (16 regions)</summary>
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
      <td>8</td>
      <td>1</td>
      <td>8</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>9</td>
      <td>35</td>
      <td>9</td>
      <td>35</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>36</td>
      <td>48</td>
      <td>36</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>75</td>
      <td>49</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>99</td>
      <td>76</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>124</td>
      <td>100</td>
      <td>124</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>125</td>
      <td>235</td>
      <td>125</td>
      <td>235</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>242</td>
      <td>250</td>
      <td>242</td>
      <td>250</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>251</td>
      <td>257</td>
      <td>251</td>
      <td>257</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>258</td>
      <td>264</td>
      <td>258</td>
      <td>264</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>265</td>
      <td>287</td>
      <td>265</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>295</td>
      <td>288</td>
      <td>295</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>296</td>
      <td>318</td>
      <td>296</td>
      <td>318</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>319</td>
      <td>326</td>
      <td>319</td>
      <td>326</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>327</td>
      <td>347</td>
      <td>327</td>
      <td>347</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>348</td>
      <td>356</td>
      <td>348</td>
      <td>356</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mit">6MIT</a> — Chain G (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MQAF</span><span class="topo-outside">GV</span><span class="topo-unknown">LDRYIG</span><span class="topo-membrane">KTIFTTIMMTLFMLVSLSGIIKFVDQLK</span><span class="topo-inside">KAGQGSYD</span><span class="topo-membrane">ALGAGMYTLLSVPKDVQIFFPMAALLGALLGL</span><span class="topo-outside">GMLAQRSELVVMQASGFTRLQVA</span><span class="topo-membrane">LSVMKTAIPLVLLTMAI</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GEWVAPQGE</span><span class="topo-inside">QMARNYRAQAMYGGSLLSTQQGLWAKDGQNFVYIERVKGDDELGGVSIYAFNDERRLQSVRHASSAKFDPEHKQWRLSQVDESDLTNPKQITGSQTVSGTWKTNLTPDKLG</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">VVALDPDALSISGLHNYVKYLKSSGQDAGRYQL</span><span class="topo-membrane">NMWSKIFQPMSVAVMMLMALSFI</span><span class="topo-outside">FGPLRSVPM</span><span class="topo-membrane">GVRVVTGISFGFVFYVLDQIFG</span><span class="topo-inside">PLTLVYGIPPI</span><span class="topo-membrane">IGALLPSASFLLISLWLLLKR</span><span class="topo-unknown">S</span></span>
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
      <td>5</td>
      <td>6</td>
      <td>5</td>
      <td>6</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>7</td>
      <td>12</td>
      <td>7</td>
      <td>12</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>13</td>
      <td>40</td>
      <td>13</td>
      <td>40</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>41</td>
      <td>48</td>
      <td>41</td>
      <td>48</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>49</td>
      <td>80</td>
      <td>49</td>
      <td>80</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>81</td>
      <td>103</td>
      <td>81</td>
      <td>103</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>104</td>
      <td>129</td>
      <td>104</td>
      <td>129</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>130</td>
      <td>273</td>
      <td>130</td>
      <td>273</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>274</td>
      <td>296</td>
      <td>274</td>
      <td>296</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>297</td>
      <td>305</td>
      <td>297</td>
      <td>305</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>306</td>
      <td>327</td>
      <td>306</td>
      <td>327</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>328</td>
      <td>338</td>
      <td>328</td>
      <td>338</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>339</td>
      <td>359</td>
      <td>339</td>
      <td>359</td>
      <td>Membrane</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mjp">6MJP</a> — Chain A (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AILKAQHLAKSYKKRKVVSDVSLQVESGQIVGLLGPNGAGKTTSFYMIVGLVARDEGTITIDDNDISILPMHSRSRMGIGYLPQEASIFRKLSVEDNIMAVLQTREELTHEERQDKLED</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LLEEFHIQHIRKSAGMALSGGERRRVEIARALAANPQFILLDQPFAGVDPISVIDIKKIIEHLRDRGLGVLITDHNVRETLDVCEKAYIVSQGRLIAEGTPQDVLNNEQVKQVYLGEQFR</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-inside">L</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>2</td>
      <td>241</td>
      <td>2</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mjp">6MJP</a> — Chain B (0 TMs, non_tm)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">AILKAQHLAKSYKKRKVVSDVSLQVESGQIVGLLGPNGAGKTTSFYMIVGLVARDEGTITIDDNDISILPMHSRSRMGIGYLPQEASIFRKLSVEDNIMAVLQTREELTHEERQDKLED</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">LLEEFHIQHIRKSAGMALSGGERRRVEIARALAANPQFILLDQPFAGVDPISVIDIKKIIEHLRDRGLGVLITDHNVRETLDVCEKAYIVSQGRLIAEGTPQDVLNNEQVKQVYLGEQFR</span></span>
<span class="topo-ruler"> </span>
<span class="topo-line"><span class="topo-inside">L</span></span>
<details class="topo-details"><summary>Topology coordinates (1 regions)</summary>
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
      <td>2</td>
      <td>241</td>
      <td>2</td>
      <td>241</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mjp">6MJP</a> — Chain C (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">M</span><span class="topo-inside">S</span><span class="topo-membrane">LSRIVYVLLLFIASWSLY</span><span class="topo-outside">YLLGQEQDSKIQVAPNLELPMFSGENLENISYDEQGIRNYVITSIHLDHYAKSGNTLFKAPILKVYREGTLQEWEITARRGILSKDQVLTLYDDVLAKNL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190 </span>
<span class="topo-line"><span class="topo-outside">LPDSGFDTLTTSEMSIQLKSRDFWADKPVELRGPQFETHGQAMKGNFADHSAELY</span><span class="topo-unknown">NQVQGRYETLTPLVPR</span></span>
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
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>20</td>
      <td>3</td>
      <td>20</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>21</td>
      <td>175</td>
      <td>21</td>
      <td>175</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mjp">6MJP</a> — Chain F (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MIIVRYLIRET</span><span class="topo-membrane">IKSQFAIFFVLFLVFLSQKFI</span><span class="topo-outside">RVLAD</span><span class="topo-unknown">ASDGEIPTS</span><span class="topo-outside">M</span><span class="topo-unknown">ILSIVGLN</span><span class="topo-membrane">MPAMGLLMLPLSLYIGILLT</span><span class="topo-inside">FGRLYAESEITVMNATGIGNKFLI</span><span class="topo-membrane">RAALYLALITASVAAFNALWL</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">A</span><span class="topo-outside">PWSQDKEAHLMEQFA</span><span class="topo-unknown">AENSV</span><span class="topo-outside">DLLQKGHFQRSPDGSSVVFIDNIENRKLYNVFVAQLAPRDSILPSVMFSHSGDVKE</span><span class="topo-unknown">LS</span><span class="topo-outside">DGRQIITLYDGTRYEGVPTRVDYMITNFDSYDGLIGQ</span><span class="topo-unknown">REVK</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-unknown">SA</span><span class="topo-outside">ERDWEALPTLSLLNNADRRAQAELQ</span><span class="topo-membrane">WRISLVVCIPLLTMLVVPLS</span><span class="topo-inside">AVNPRQGRF</span><span class="topo-membrane">AKMGPAILIYLTYFLALSAT</span><span class="topo-outside">KSAIEDGSLPVII</span><span class="topo-membrane">GLWPINAALLLAALMVNTL</span><span class="topo-inside">DS</span><span class="topo-unknown">IPVRRFKDRW</span></span>
<span class="topo-ruler">      </span>
<span class="topo-line"><span class="topo-unknown">KQ</span><span class="topo-inside">R</span><span class="topo-unknown">KVA</span></span>
<details class="topo-details"><summary>Topology coordinates (20 regions)</summary>
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
      <td>11</td>
      <td>1</td>
      <td>11</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>12</td>
      <td>32</td>
      <td>12</td>
      <td>32</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>33</td>
      <td>37</td>
      <td>33</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>47</td>
      <td>47</td>
      <td>47</td>
      <td>47</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>55</td>
      <td>48</td>
      <td>55</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>56</td>
      <td>75</td>
      <td>56</td>
      <td>75</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>76</td>
      <td>99</td>
      <td>76</td>
      <td>99</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>121</td>
      <td>100</td>
      <td>121</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>122</td>
      <td>136</td>
      <td>122</td>
      <td>136</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>142</td>
      <td>197</td>
      <td>142</td>
      <td>197</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>200</td>
      <td>236</td>
      <td>200</td>
      <td>236</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>267</td>
      <td>243</td>
      <td>267</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>268</td>
      <td>287</td>
      <td>268</td>
      <td>287</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>288</td>
      <td>296</td>
      <td>288</td>
      <td>296</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>297</td>
      <td>316</td>
      <td>297</td>
      <td>316</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>317</td>
      <td>329</td>
      <td>317</td>
      <td>329</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>348</td>
      <td>330</td>
      <td>348</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>349</td>
      <td>350</td>
      <td>349</td>
      <td>350</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>351</td>
      <td>362</td>
      <td>351</td>
      <td>362</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>363</td>
      <td>363</td>
      <td>363</td>
      <td>363</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6mjp">6MJP</a> — Chain G (6 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MFKILDWYIGRTI</span><span class="topo-membrane">VATTALVLVTFVGLSGIIKYVEQL</span><span class="topo-outside">RKVGEGSYDL</span><span class="topo-membrane">LQALLFVVLSIPRDVEMFFPMAALLGALI</span><span class="topo-inside">GLGALASSSELVVMQAAGFSKLDIGLSV</span><span class="topo-membrane">LKTAIPLMIIVTLLGE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">WGAPQAQ</span><span class="topo-outside">KMARDMRAFATSGGAI</span><span class="topo-unknown">MS</span><span class="topo-outside">VRTGVWARDANDFIFIAKVENEHLYGLNLWRFDENKKLSTVIFSEQVDYVANNEWLMKDAVLTRLVNDIEISKESLPEYRWRTSLAPDKLAVVTV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350      </span>
<span class="topo-line"><span class="topo-outside">KPEELSLTGLSDYVHYLKASEQDSSRYELA</span><span class="topo-membrane">LWRKVTQPISIAVMMLMALSF</span><span class="topo-inside">IFGPLRSVTMG</span><span class="topo-membrane">ARILSGVIAGFSFYISSEFFG</span><span class="topo-outside">PLSLVYGLPPL</span><span class="topo-membrane">FGALAPSLVFLAIALGLLG</span><span class="topo-inside">RKL</span></span>
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
      <td>13</td>
      <td>1</td>
      <td>13</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>14</td>
      <td>37</td>
      <td>14</td>
      <td>37</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>38</td>
      <td>47</td>
      <td>38</td>
      <td>47</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>48</td>
      <td>76</td>
      <td>48</td>
      <td>76</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>77</td>
      <td>104</td>
      <td>77</td>
      <td>104</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>127</td>
      <td>105</td>
      <td>127</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>128</td>
      <td>143</td>
      <td>128</td>
      <td>143</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>146</td>
      <td>270</td>
      <td>146</td>
      <td>270</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>271</td>
      <td>291</td>
      <td>271</td>
      <td>291</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>292</td>
      <td>302</td>
      <td>292</td>
      <td>302</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>303</td>
      <td>323</td>
      <td>303</td>
      <td>323</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>324</td>
      <td>334</td>
      <td>324</td>
      <td>334</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>335</td>
      <td>353</td>
      <td>335</td>
      <td>353</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>354</td>
      <td>356</td>
      <td>354</td>
      <td>356</td>
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

### LptC inserts a transmembrane helix into the transporter core, breaking pseudosymmetry

LptC, an accessory protein with a single transmembrane helix, inserts this helix between LptG TM1 and LptF TM5 in the ABC transporter, breaking the two-fold pseudosymmetry of the LptB2FG core. This defines a single entry path for LPS between LptG TM1 and LptF TM5, while the alternate path (between LptG TM5 and LptF TM1) is blocked by the convex surface of the LptC-LptF beta-jellyroll. No other ABC system incorporates a transmembrane helix from a separate protein directly into the transporter core.

### ATP-independent entry into the cavity

LPS entry into the transporter cavity does not require ATP hydrolysis. Crosslinking experiments showed LPS binding at the base of the cavity (near LptC TM helix) in both active and inactive (LptB E163Q) complexes. However, ATP-dependent extraction moves LPS from the membrane into the beta-jellyroll domain of LptF and LptC. This two-step mechanism separates substrate entry from energy-dependent translocation.

### LptF gate prevents backward LPS flow

The beta-jellyroll domain of LptF exists in two conformations: open (E. cloacae structure) and closed (V. cholerae structure). A disulfide crosslink trapping LptF in the closed state prevented LPS transport but not ATP hydrolysis, demonstrating that gate-opening is not directly coupled to ATP hydrolysis. Gate closure behind the substrate provides a mechanism to prevent backward flow when the cavity reopens, ensuring unidirectional transport.

### LptC TM helix modulates ATPase efficiency

The LptC TM helix coordinates ATP hydrolysis with LPS extraction from the membrane. Complexes with Delta-TM LptC showed substantially higher ATPase activity compared to full-length LptB2FGC, yet supported comparable LPS transport to LptA. This suggests the TM domain of LptC modulates ATP hydrolysis to achieve more efficient coupling of ATP consumption and LPS movement, providing a fitness advantage that is conserved in the wild.

### Structural model of LPS transport

(1) Newly synthesized LPS binds at the entry point defined by the LptC TM segment intercalated between LptG TM1 and LptF TM5. (2) ATP-independent entry of LPS into the cavity occurs past the LptC TM segment. (3) ATP-dependent cavity constriction provides the force to push LPS out of the membrane. (4) The LptC TM helix coordinates ATP hydrolysis with membrane extraction. (5) The LptF beta-jellyroll gate closes behind the substrate, preventing backward flow. (6) LPS moves from LptC to LptA and through LptDE to the outer membrane.


## Cross-References

- <a href="/xray-mp-wiki/concepts/lps-transport/">LPS Transport</a> — LptB2FGC is the inner membrane motor for LPS transport in Gram-negative bacteria
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Ni-NTA affinity chromatography used for purification of His-tagged complex
- <a href="/xray-mp-wiki/methods/crystallization/hanging-drop-vapor-diffusion/">Hanging Drop Vapor Diffusion</a> — E. cloacae LptB2FGC crystallized by hanging-drop vapor diffusion
- <a href="/xray-mp-wiki/methods/crystallization/sitting-drop-vapor-diffusion/">Sitting Drop Vapor Diffusion</a> — V. cholerae LptB2FGC crystallized by sitting-drop vapor diffusion
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iptg/">IPTG</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/peg-400/">PEG400</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> — Additive used in purification or crystallization buffers
