---
title: "E. coli YajC Transmembrane Protein"
created: 2026-05-28
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1016##j.str.2007.09.023]
verified: false
---

# E. coli YajC Transmembrane Protein

## Overview

YajC is a single transmembrane (TM) protein from Escherichia coli that associates with the [AcrB multidrug efflux pump](/xray-mp-wiki/proteins/abc-transporters/acrb/). The crystal structure of the [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/):YajC complex (PDB 2RDD) revealed YajC as a single elongated TM helix of approximately 37 residues that docks into a highly conserved cavity on the surface of the [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) trimer. YajC interacts with TM helices 2, 7, 11, 12, and Iα2 of [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/). Deletion of yajc in E. coli results in a modest increase in susceptibility to beta-lactam antibiotics, suggesting a functional role in the AcrB-mediated efflux system. YajC is known to also interact with SecD and SecF, components of the protein translocase machinery.


## Publications

### doi/10.1016##j.str.2007.09.023

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a></td>
      <td>3.5 A</td>
      <td>P3221</td>
      <td>YajC single transmembrane helix (residues 20-40 modeled), associated with <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">ACRB</a> trimer</td>
      <td><a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: E. coli (endogenous)
- **Construct**: Wild-type YajC, endogenous expression from JM109 strain
- **Notes**: YajC was identified as the novel TM subunit copurifying with endogenous [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/). The transmembrane region was predicted to cover residues 20-40 with the C terminus on the cytoplasmic side. N-terminal (18 residues) and C-terminal (56 residues) were not modeled due to lack of electron density.

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
      <td>Cell culture and membrane isolation</td>
      <td>Cell disruption with X-Press, membrane fractions collected by ultracentrifugation at 185,000 x g for 90 min</td>
      <td>--</td>
      <td>-- + --</td>
      <td>E. coli JM109 strain grown in LB media with 100 mg/L <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> for 16 hr</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Membrane solubilization</td>
      <td>--</td>
      <td>-- + 1.75% n-Dodecyl-beta-D-maltopyranoside (<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>)</td>
      <td>Membranes solubilized in 1.75% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (Anatrace)</td>
    </tr>
    <tr>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> (Chelating Sepharose Fast Flow)</td>
      <td>Chelating Sepharose Fast Flow (GE Healthcare)</td>
      <td>60 mM NaPO4 (pH 7.5), 0.7 M NaCl, 33 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">ACRB</a> bound to Ni2+ media overnight; unbound material washed out. Endogenous <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">ACRB</a> co-purified with YajC transmembrane subunit.</td>
    </tr>
    <tr>
      <td>Elution</td>
      <td>Ni-<a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> elution</td>
      <td>Chelating Sepharose Fast Flow (GE Healthcare)</td>
      <td>30 mM NaPO4 (pH 7.5), 0.1 M NaCl, 10 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 1 mM <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> (elution with 150 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>) + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td><a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">ACRB</a> eluted with 150 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> (Sephacryl S300 16/60)</td>
      <td>Sephacryl S300 16/60 (GE Healthcare)</td>
      <td>20 mM HEPES (pH 7.0), 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>SEC used to improve sample homogeneity. Protein concentrated to 10 mg/mL prior to crystallization.</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Hanging-drop vapor diffusion</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>10 mg/mL <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">ACRB</a>:YajC complex in 20 mM HEPES (pH 7.0), 150 mM NaCl, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>14%-28% PEG1000 or PEG1500, 0.1 M Tris (pH 7.5), 0.1 M Li2SO4, 18 mM n-Octyl-beta-D-Thioglucopyranoside, 20% 1,2,3-heptanetriol</td>
    </tr>
    <tr>
      <td>Mixing ratio</td>
      <td>equal volumes protein to reservoir</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>293 K</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-4 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% w/v <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> in reservoir solution, 2 min incubation</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals reached maximum size of 0.4 x 0.2 x 0.2 mm. Data collected at 100 K at ESRF ID14-2 beamline. Space group P3221 with unit cell dimensions a=145.1, b=145.1, c=511.6 A, alpha=90, beta=90, gamma=120. Rcryst 27.9%, Rfree 31.7%. The structure revealed YajC as a 37-residue single TM helix interacting with TM helices 2, 7, 11, 12, and Iα2 of <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">ACRB</a>. Six <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> molecules were observed bound in the central cavity of the <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">ACRB</a> trimer.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDTVTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGSQYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLA</span><span class="topo-unknown">TG</span><span class="topo-outside">ANALDTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVMAEEGLPPKEATRKSMGQIQG</span><span class="topo-membrane">ALVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAK</span><span class="topo-unknown">GDHGEGK</span><span class="topo-inside">KGFFGW</span><span class="topo-unknown">FNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGRY</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKDAMVFAFNLPAIVE</span><span class="topo-unknown">LGTATG</span><span class="topo-outside">FDFELIDQAGLGHEKLTQARNQLLAEAAKHPDM</span><span class="topo-unknown">LTS</span><span class="topo-outside">VRPNG</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYRMLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAAL</span><span class="topo-inside">YES</span><span class="topo-membrane">WSIPFSVMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040         </span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIFFV</span><span class="topo-unknown">PVFFVVVR</span><span class="topo-inside">RRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHH</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>294</td>
      <td>27</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>296</td>
      <td>295</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>297</td>
      <td>340</td>
      <td>297</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>412</td>
      <td>398</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>440</td>
      <td>413</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>456</td>
      <td>441</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>502</td>
      <td>490</td>
      <td>502</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>510</td>
      <td>515</td>
      <td>510</td>
      <td>515</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>536</td>
      <td>516</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>673</td>
      <td>557</td>
      <td>673</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>679</td>
      <td>674</td>
      <td>679</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>680</td>
      <td>712</td>
      <td>680</td>
      <td>712</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>713</td>
      <td>715</td>
      <td>713</td>
      <td>715</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>716</td>
      <td>876</td>
      <td>716</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>891</td>
      <td>877</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>894</td>
      <td>892</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>918</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>929</td>
      <td>919</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>944</td>
      <td>930</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1030</td>
      <td>1023</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1036</td>
      <td>1031</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1049</td>
      <td>1037</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain B (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30       </span>
<span class="topo-line"><span class="topo-outside">SP</span><span class="topo-membrane">MSLILMLVVFGLIFYFMILRPQQK</span><span class="topo-inside">RTKEHKKLMDS</span></span>
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
      <td>2</td>
      <td>19</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>26</td>
      <td>21</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>37</td>
      <td>45</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain C (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDTVTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGSQYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLA</span><span class="topo-unknown">TG</span><span class="topo-outside">ANALDTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVMAEEGLPPKEATRKSMGQIQG</span><span class="topo-membrane">ALVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAK</span><span class="topo-unknown">GDHGEGK</span><span class="topo-inside">KGFFGW</span><span class="topo-unknown">FNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGRY</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKDAMVFAFNLPAIVE</span><span class="topo-unknown">LGTATG</span><span class="topo-outside">FDFELIDQAGLGHEKLTQARNQLLAEAAKHPDM</span><span class="topo-unknown">LTS</span><span class="topo-outside">VRPNG</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYRMLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAAL</span><span class="topo-inside">YES</span><span class="topo-membrane">WSIPFSVMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040         </span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIFFV</span><span class="topo-unknown">PVFFVVVR</span><span class="topo-inside">RRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHH</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>294</td>
      <td>27</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>296</td>
      <td>295</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>297</td>
      <td>340</td>
      <td>297</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>412</td>
      <td>398</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>440</td>
      <td>413</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>456</td>
      <td>441</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>502</td>
      <td>490</td>
      <td>502</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>510</td>
      <td>515</td>
      <td>510</td>
      <td>515</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>536</td>
      <td>516</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>673</td>
      <td>557</td>
      <td>673</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>679</td>
      <td>674</td>
      <td>679</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>680</td>
      <td>712</td>
      <td>680</td>
      <td>712</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>713</td>
      <td>715</td>
      <td>713</td>
      <td>715</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>716</td>
      <td>876</td>
      <td>716</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>891</td>
      <td>877</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>894</td>
      <td>892</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>918</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>929</td>
      <td>919</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>944</td>
      <td>930</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1030</td>
      <td>1023</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1036</td>
      <td>1031</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1049</td>
      <td>1037</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain D (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30       </span>
<span class="topo-line"><span class="topo-outside">SP</span><span class="topo-membrane">MSLILMLVVFGLIFYFMILRPQQK</span><span class="topo-inside">RTKEHKKLMDS</span></span>
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
      <td>2</td>
      <td>19</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>26</td>
      <td>21</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>37</td>
      <td>45</td>
      <td>55</td>
      <td>Inside</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain E (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-inside">MPNFFIDRPI</span><span class="topo-membrane">FAWVIAIIIMLAGGLA</span><span class="topo-outside">ILKLPVAQYPTIAPPAVTISASYPGADAKTVQDTVTQVIEQNMNGIDNLMYMSSNSDSTGTVQITLTFESGTDADIAQVQVQNKLQLAMPLLPQ</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-outside">EVQQQGVSVEKSSSSFLMVVGVINTDGTMTQEDISDYVAANMKDAISRTSGVGDVQLFGSQYAMRIWMNPNELNKFQLTPVDVITAIKAQNAQVAAGQLGGTPPVKGQQLNASIIAQTRL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">TSTEEFGKILLKVNQDGSRVLLRDVAKIELGGENYDIIAEFNGQPASGLGIKLA</span><span class="topo-unknown">TG</span><span class="topo-outside">ANALDTAAAIRAELAKMEPFFPSGLKIVYPYDTTPFVKISIHEV</span><span class="topo-membrane">VKTLVEAIILVFLVMYL</span><span class="topo-inside">FLQ</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">NFRAT</span><span class="topo-membrane">LIPTIAVPVVLLGTFAVL</span><span class="topo-outside">AAFGFSINTLTMFG</span><span class="topo-membrane">MVLAIGLLVDDAIVV</span><span class="topo-inside">VENVERVMAEEGLPPKEATRKSMGQIQG</span><span class="topo-membrane">ALVGIAMVLSAVFVPM</span><span class="topo-outside">AFFGGSTGAIYRQFS</span><span class="topo-membrane">ITIVSAMAL</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-membrane">SVLVALILT</span><span class="topo-inside">PALCATMLKPIAK</span><span class="topo-unknown">GDHGEGK</span><span class="topo-inside">KGFFGW</span><span class="topo-unknown">FNRMFEKSTHHYTDSVGGILR</span><span class="topo-inside">STGRY</span><span class="topo-membrane">LVLYLIIVVGMAYLF</span><span class="topo-outside">VRLPSSFLPDEDQGVFMTMVQLPAGATQERTQKVLNEVTHYYLT</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680       690       700       710       720</span>
<span class="topo-line"><span class="topo-outside">KEKNNVESVFAVNGFGFAGRGQNTGIAFVSLKDWADRPGEENKVEAITMRATRAFSQIKDAMVFAFNLPAIVE</span><span class="topo-unknown">LGTATG</span><span class="topo-outside">FDFELIDQAGLGHEKLTQARNQLLAEAAKHPDM</span><span class="topo-unknown">LTS</span><span class="topo-outside">VRPNG</span></span>
<span class="topo-ruler">       730       740       750       760       770       780       790       800       810       820       830       840</span>
<span class="topo-line"><span class="topo-outside">LEDTPQFKIDIDQEKAQALGVSINDINTTLGAAWGGSYVNDFIDRGRVKKVYVMSEAKYRMLPDDIGDWYVRAADGQMVPFSAFSSSRWEYGSPRLERYNGLPSMEILGQAAPGKSTGEA</span></span>
<span class="topo-ruler">       850       860       870       880       890       900       910       920       930       940       950       960</span>
<span class="topo-line"><span class="topo-outside">MELMEQLASKLPTGVGYDWTGMSYQERLSGNQAPSL</span><span class="topo-membrane">YAISLIVVFLCLAAL</span><span class="topo-inside">YES</span><span class="topo-membrane">WSIPFSVMLVVPLGVIGALLAATF</span><span class="topo-outside">RGLTNDVYFQV</span><span class="topo-membrane">GLLTTIGLSAKNAIL</span><span class="topo-inside">IVEFAKDLMDKEGKG</span><span class="topo-unknown">L</span></span>
<span class="topo-ruler">       970       980       990      1000      1010      1020      1030      1040         </span>
<span class="topo-line"><span class="topo-unknown">IEATLDAVRM</span><span class="topo-inside">RLRP</span><span class="topo-membrane">ILMTSLAFILGVMPLVI</span><span class="topo-outside">STGAGSGAQNAV</span><span class="topo-membrane">GTGVMGGMVTATVLAIFFV</span><span class="topo-unknown">PVFFVVVR</span><span class="topo-inside">RRFSRK</span><span class="topo-unknown">NEDIEHSHTVDHH</span></span>
<details class="topo-details"><summary>Topology coordinates (39 regions)</summary>
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
      <td>10</td>
      <td>1</td>
      <td>10</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>11</td>
      <td>26</td>
      <td>11</td>
      <td>26</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>294</td>
      <td>27</td>
      <td>294</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>295</td>
      <td>296</td>
      <td>295</td>
      <td>296</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>297</td>
      <td>340</td>
      <td>297</td>
      <td>340</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>341</td>
      <td>357</td>
      <td>341</td>
      <td>357</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>358</td>
      <td>365</td>
      <td>358</td>
      <td>365</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>366</td>
      <td>383</td>
      <td>366</td>
      <td>383</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>384</td>
      <td>397</td>
      <td>384</td>
      <td>397</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>398</td>
      <td>412</td>
      <td>398</td>
      <td>412</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>413</td>
      <td>440</td>
      <td>413</td>
      <td>440</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>441</td>
      <td>456</td>
      <td>441</td>
      <td>456</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>457</td>
      <td>471</td>
      <td>457</td>
      <td>471</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>472</td>
      <td>489</td>
      <td>472</td>
      <td>489</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>490</td>
      <td>502</td>
      <td>490</td>
      <td>502</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>503</td>
      <td>509</td>
      <td>503</td>
      <td>509</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>510</td>
      <td>515</td>
      <td>510</td>
      <td>515</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>516</td>
      <td>536</td>
      <td>516</td>
      <td>536</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>537</td>
      <td>541</td>
      <td>537</td>
      <td>541</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>542</td>
      <td>556</td>
      <td>542</td>
      <td>556</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>557</td>
      <td>673</td>
      <td>557</td>
      <td>673</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>674</td>
      <td>679</td>
      <td>674</td>
      <td>679</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>680</td>
      <td>712</td>
      <td>680</td>
      <td>712</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>713</td>
      <td>715</td>
      <td>713</td>
      <td>715</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>716</td>
      <td>876</td>
      <td>716</td>
      <td>876</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>877</td>
      <td>891</td>
      <td>877</td>
      <td>891</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>892</td>
      <td>894</td>
      <td>892</td>
      <td>894</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>895</td>
      <td>918</td>
      <td>895</td>
      <td>918</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>919</td>
      <td>929</td>
      <td>919</td>
      <td>929</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>930</td>
      <td>944</td>
      <td>930</td>
      <td>944</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>945</td>
      <td>959</td>
      <td>945</td>
      <td>959</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>960</td>
      <td>970</td>
      <td>960</td>
      <td>970</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>971</td>
      <td>974</td>
      <td>971</td>
      <td>974</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>975</td>
      <td>991</td>
      <td>975</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1003</td>
      <td>992</td>
      <td>1003</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1004</td>
      <td>1022</td>
      <td>1004</td>
      <td>1022</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>1023</td>
      <td>1030</td>
      <td>1023</td>
      <td>1030</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>1031</td>
      <td>1036</td>
      <td>1031</td>
      <td>1036</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>1037</td>
      <td>1049</td>
      <td>1037</td>
      <td>1049</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/2rdd">2RDD</a> — Chain F (1 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30       </span>
<span class="topo-line"><span class="topo-outside">SP</span><span class="topo-membrane">MSLILMLVVFGLIFYFMILRPQQK</span><span class="topo-inside">RTKEHKKLMDS</span></span>
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
      <td>2</td>
      <td>19</td>
      <td>20</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>3</td>
      <td>26</td>
      <td>21</td>
      <td>44</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>27</td>
      <td>37</td>
      <td>45</td>
      <td>55</td>
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

### YajC interaction with AcrB

YajC associates with the [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) trimer as a single elongated transmembrane helix that
is approximately 54 A long and extends across the entire width of the membrane. The
helix is highly tilted with respect to the membrane plane. YajC docks into a cavity
formed by TM helices 2, 7, 11, 12, and Iα2 of [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/). The average Cα-to-Cα distance
from YajC to [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) is 7.3 A, comparable to the distance between the gamma subunit and
the TM helix bundle of the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) complex (6.5 A). The binding interface on [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) is one
of the most conserved regions on its surface, suggesting that YajC:[ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) interaction
may be found in species other than E. coli.

### Conformational twist of the AcrB porter domain

The [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/):YajC complex structure revealed a significant rotation of the [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) porter
domain relative to its transmembrane domain. This twist is consistent with the
"twist-to-open" hypothesis for TolC activation, where a specific rotation of the
porter domain could be communicated by [ACRA](/xray-mp-wiki/proteins/abc-transporters/acra/) to the superhelical coils of TolC near
the equatorial domain, inducing a twist that opens the exit duct. This represents
another dynamic motion inherent to [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/), complementary to the cyclic peristaltic
mechanism revealed by asymmetric structures.

### Functional role of YajC in drug resistance

Growth experiments with yajc-deleted E. coli strains showed a modest increase in
susceptibility to beta-lactam antibiotics ([Ampicillin](/xray-mp-wiki/reagents/antibiotics/ampicillin/) and [Nafcillin](/xray-mp-wiki/reagents/antibiotics/nafcillin/)). However, the
magnitude of this effect did not scale with the relative [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) transport affinity of
the different beta-lactams, and the functional role of the YajC:[ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) interaction
could not be conclusively assigned. The enhanced susceptibility cannot arise from
failure to translocate beta-lactamase into the periplasm since the deletion strain
does not contain any beta-lactamase.

### YajC classification and conservation

YajC was assigned by mass spectrometry as the novel TM subunit of [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/). Three
independent mass spectrometry approaches confirmed YajC as the only plausible
candidate. The transmembrane region was predicted by MEMSAT3, Phobius, and TMHMM
to cover residues 20-40. The sequence shows modest homology (14% identical) to the
gamma subunit of the [SECY](/xray-mp-wiki/proteins/secretion-translocon/secy/) complex, which shares a similar structural arrangement.
SecD and SecF, which are known to interact with YajC, are classified as RND
transporters and are fused into a single polypeptide forming an arrangement similar
to [ACRB](/xray-mp-wiki/proteins/abc-transporters/acrb/) in certain bacteria.


## Cross-References

- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">AcrB multidrug efflux pump</a> — YajC forms a stable complex with AcrB; crystal structure determined together (PDB 2RDD)
- <a href="/xray-mp-wiki/proteins/abc-transporters/acra/">AcrA multidrug efflux pump periplasmic protein</a> — AcrA is the periplasmic adaptor in the AcrAB-TolC efflux complex; hypothesized to interact with YajC
- <a href="/xray-mp-wiki/proteins/secretion-translocon/secy/">Thermus thermophilus SecY Core Channel Subunit</a> — YajC structural analogy with the gamma subunit of the SecY translocation channel
- <a href="/xray-mp-wiki/reagents/antibiotics/ampicillin/">Ampicillin</a> — Ampicillin co-crystallized with AcrB:YajC complex; six molecules observed in the central cavity
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">n-Dodecyl-beta-D-maltopyranoside (DDM)</a> — DDM used for solubilization and purification of the AcrB:YajC complex
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/methods/purification/size-exclusion-chromatography/">Size-Exclusion Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/proteins/abc-transporters/acrb/">ACRB</a> — Related protein structure
- <a href="/xray-mp-wiki/reagents/additives/beta-mercaptoethanol/">beta-Mercaptoethanol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
