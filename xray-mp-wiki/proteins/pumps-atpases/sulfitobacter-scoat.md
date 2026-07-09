---
title: "sCoaT (Co2+/Zn2+-transporting PIB-4-ATPase from Sulfitobacter sp. NAS14-1)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [pump, membrane-protein, xray-crystallography]
sources: [doi/10.7554##eLife.73124]
verified: regex
uniprot_id: A3T2G5
---

# sCoaT (Co2+/Zn2+-transporting PIB-4-ATPase from Sulfitobacter sp. NAS14-1)

<div class="expr-badges"><span class="expr-badge expr-e-coli">E. coli</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/A3T2G5">UniProt: A3T2G5</a>

<span class="expr-badge">Sulfitobacter sp. (strain NAS-14.1)</span>

## Overview

sCoaT is a PIB-4-type ATPase from Sulfitobacter sp. NAS14-1 (UniProt ID A3T2G5) that functions as a heavy metal transporter for zinc, cadmium, and cobalt. It belongs to the P1B-4 subclass of [P-type ATPases](/xray-mp-wiki/concepts/protein-families/p-type-atpase/), which have the broadest cargo scope among heavy-metal transporting P-type ATPases. The protein was expressed in [Escherichia coli](/xray-mp-wiki/concepts/methods-techniques/c41-e-coli-expression-strain/) C41 cells, purified using Ni2+-NTA affinity chromatography and gel filtration, and crystallized using the [HiLiDe method](/xray-mp-wiki/methods/crystallization/hilide-crystallization/). The structures were determined at 3.1 and 3.3 A resolution by molecular replacement using SsZntA as a search model. The protein has eight transmembrane helices (MA, MB, M1-M6) and lacks classical heavy-metal-binding domains (HMBDs). Key findings include a histidine (H657) that serves as an internal counterion and a dual role in ion release, and the identification of novel inhibitors with antimycobacterial activity. The crystal packing features type I crystals with unrestrained transmembrane domains and minimal contacts between membrane-spanning regions. 

## Publications

### doi/10.7554##eLife.73124

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7qbz">7QBZ</a></td>
      <td>3.3</td>
      <td>P 21 21 2</td>
      <td>Full-length sCoaT from Sulfitobacter sp. NAS14-1 (UniProt A3T2G5), expressed in E. coli C41, purified by Ni2+-NTA affinity chromatography and gel filtration, crystallized with AlF4- analogue</td>
      <td>AlF4-</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/7qc0">7QC0</a></td>
      <td>3.1</td>
      <td>P 21 21 2</td>
      <td>Full-length sCoaT from Sulfitobacter sp. NAS14-1 (UniProt A3T2G5), expressed in E. coli C41, purified by Ni2+-NTA and gel filtration, crystallized with BeF3- analogue</td>
      <td>BeF3-</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Escherichia coli C41(DE3) cells
- **Construct**: sCoaT from Sulfitobacter sp. NAS14-1 (NAS141_02821) expressed with 1 mM IPTG at 18 C for 16 h
- **Notes**: Cells cultured in LB medium at 37 C until OD600 = 0.6-1, cooled to 18 C, induced with 1 mM IPTG. Resuspended in 20 mM Tris-HCl pH 7.6, 200 mM KCl, 20% glycerol, 5 mM BME. Lysed by high-pressure homogenizer at 25,000 psi with 5 mM MgCl2, 1 mM PMSF, 2 ug/ml DNase I, Roche protease inhibitor cocktail.

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
      <td>Differential centrifugation</td>
      <td>--</td>
      <td>20 mM Tris-HCl pH 7.6, 200 mM KCl, 1 mM MgCl2, 5 mM BME, 20% (vol/vol) glycerol + --</td>
      <td>Membranes isolated by ultracentrifugation at 185,500 x g for 3 h at 4 C</td>
    </tr>
    <tr>
      <td>Solubilization</td>
      <td>Detergent solubilization</td>
      <td>--</td>
      <td>20 mM Tris-HCl pH 7.6, 200 mM KCl, 1 mM MgCl2, 5 mM BME, 20% (vol/vol) glycerol + 1% (w/v) DDM</td>
      <td>3 mg/ml total protein, gentle stirring for 2 h at 4 C. Unsolubilized material removed by ultracentrifugation at 185,500 x g for 1 h. Supplemented with 30 mM imidazole and 500 mM KCl (final).</td>
    </tr>
    <tr>
      <td>Ni2+-NTA affinity chromatography</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a> (IMAC)</td>
      <td>Ni2+-NTA (HiTrap Chelating HP, 5 ml)</td>
      <td>20 mM Tris-HCl pH 7.6, 200 mM KCl, 1 mM MgCl2, 5 mM BME, 20% (vol/vol) glycerol, 0.15 mg/ml C12E8 + 0.15 mg/ml C12E8</td>
      <td>Protein from 6 l cells per column. Eluted with 400 mM imidazole gradient.</td>
    </tr>
    <tr>
      <td>Gel filtration</td>
      <td>Size-exclusion chromatography</td>
      <td>Superose 6 10/300 GL</td>
      <td>20 mM MOPS-KOH pH 6.8, 80 mM KCl, 20% (vol/vol) glycerol, 1 mM MgCl2, 5 mM BME, 0.15 mg/ml C12E8 + 0.15 mg/ml C12E8</td>
      <td>Peak fractions collected and pooled for crystallization</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>HiLiDe (high lipid-detergent) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>5-8 mg/ml sCoaT in buffer D (20 mM MOPS-KOH pH 6.8, 80 mM KCl, 20% glycerol, 1 mM MgCl2, 5 mM BME, 0.15 mg/ml C12E8) supplemented with 2 mM phosphate analogue (AlF4- or BeF3-)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>100 mM MOPS pH 6.8, 0.5 M lithium acetate, 15% PEG 2K MME, 10% glycerol, 3% tert-butanol, 5% D-sorbitol, 5 mM BME</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>19</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>2-14 days</td>
    </tr>
    <tr>
      <td>Cryoprotection</td>
      <td>20% (vol/vol) glycerol (included in reservoir)</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals obtained using HiLiDe method. Type I crystal packing with unrestrained TM domains - minimal contacts between adjacent membrane-spanning regions. Crystal forming interactions likely take place through lipid-detergent molecules. Two crystal forms obtained: E2-BeF3- and E2-AlF4-, both in P 21 21 2 space group.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7qbz">7QBZ</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRKVVADLNAVEEENMPENHTPDDGHNHAHGGFLNRILGG</span><span class="topo-outside">RAE</span><span class="topo-membrane">VIFAVLCGICLLLGWLG</span><span class="topo-inside">PKYGIMSEQ</span><span class="topo-membrane">FGFGLLLAAYFFGGYFTLREAV</span><span class="topo-outside">EKISKGQ</span><span class="topo-membrane">FQIDFLMLVAASGAAILG</span><span class="topo-inside">E</span><span class="topo-membrane">WAE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GAFLLFLFSVGHAL</span><span class="topo-outside">ENYAMGRARNAVAALAGLTPDEALVRRGDKTETVLIENLLVGDIVVVRSNERLPADGFVVKGSSAVNQAPITGESAPVDKLPVDDPEFAAANLDKLTPQTRVFAGS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">INGSGSLDVQVTKLSGESTLARVVTLVAEAQTRQSPTQNFTKKF</span><span class="topo-membrane">EKIFVPCVIALAFVTSFSFL</span><span class="topo-inside">ILDETAAQS</span><span class="topo-membrane">FYRAMAVLVAASPCALAIAT</span><span class="topo-outside">PSAVLSGVARAARGGVLIKGGAPLEAM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GHLDAIAFDKTGTLTIGEPHLVEITPYGDATETELLQVSAAVEMLSDHPLAQAVVRDVKDRLGDLPSEASDFANIIGQGVSAKVDSKVVHIGKTALFESVAGLPLPDDLRGTVEAMSQNG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RTTMIVRSGDRYLGAIGLMDTPREDARSVIAALRDLGLKRMMMISGDNQNVANAVAKEVGLDTAFGDLMPEDKVTKIAALKADGGVAMVGDGVNDAPAMANATVGIAMGAAGSDVALETA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680  </span>
<span class="topo-line"><span class="topo-outside">DIALMADDLQTLPFAVGLSRKTSRIIRL</span><span class="topo-membrane">NLWFSLGVVALLIPATLFGL</span><span class="topo-inside">G</span><span class="topo-membrane">IGPAVLVHEGSTLVVVANALR</span><span class="topo-outside">LLAFKDNR</span><span class="topo-unknown">VKSA</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>40</td>
      <td>1</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>41</td>
      <td>43</td>
      <td>41</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>60</td>
      <td>44</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>69</td>
      <td>61</td>
      <td>69</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>70</td>
      <td>91</td>
      <td>70</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>98</td>
      <td>92</td>
      <td>98</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>99</td>
      <td>116</td>
      <td>99</td>
      <td>116</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>117</td>
      <td>117</td>
      <td>117</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>134</td>
      <td>118</td>
      <td>134</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>135</td>
      <td>284</td>
      <td>135</td>
      <td>284</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>285</td>
      <td>304</td>
      <td>285</td>
      <td>304</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>305</td>
      <td>313</td>
      <td>305</td>
      <td>313</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>333</td>
      <td>314</td>
      <td>333</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>334</td>
      <td>628</td>
      <td>334</td>
      <td>628</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>629</td>
      <td>648</td>
      <td>629</td>
      <td>648</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>649</td>
      <td>649</td>
      <td>649</td>
      <td>649</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>650</td>
      <td>670</td>
      <td>650</td>
      <td>670</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>671</td>
      <td>678</td>
      <td>671</td>
      <td>678</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>679</td>
      <td>682</td>
      <td>679</td>
      <td>682</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</details>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/7qc0">7QC0</a> — Chain A (8 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">MRKVVADLNAVEEENMPENHTPDDGHNHAHGGFLNRILGG</span><span class="topo-outside">RAE</span><span class="topo-membrane">VIFAVLCGICLLLGWLG</span><span class="topo-inside">PKYGIMSEQF</span><span class="topo-membrane">GFGLLLAAYFFGGYFTLREAV</span><span class="topo-outside">EKISKGQF</span><span class="topo-membrane">QIDFLMLVAASGAAILGE</span><span class="topo-inside">W</span><span class="topo-membrane">AE</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">GAFLLFLFSVGHA</span><span class="topo-outside">LENYAMGRARNAVAALAGLTPDEALVRRGDKTETVLIENLLVGDIVVVRSNERLPADGFVVKGSSAVNQAPITGESAPVDKLPVDDPEFAAANLDKLTPQTRVFAGS</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">INGSGSLDVQVTKLSGESTLARVVTLVAEAQTRQSPTQNFTKKFEKI</span><span class="topo-membrane">FVPCVIALAFVTSFSFLIL</span><span class="topo-inside">DETAA</span><span class="topo-membrane">QSFYRAMAVLVAASPCALAIA</span><span class="topo-outside">TPSAVLSGVARAARGGVLIKGGAPLEAM</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-outside">GHLDAIAFDKTGTLTIGEPHLVEITPYGDATETELLQVSAAVEMLSDHPLAQAVVRDVKDRLGDLPSEASDFANIIGQGVSAKVDSKVVHIGKTALFESVAGLPLPDDLRGTVEAMSQNG</span></span>
<span class="topo-ruler">       490       500       510       520       530       540       550       560       570       580       590       600</span>
<span class="topo-line"><span class="topo-outside">RTTMIVRSGDRYLGAIGLMDTPREDARSVIAALRDLGLKRMMMISGDNQNVANAVAKEVGLDTAFGDLMPEDKVTKIAALKADGGVAMVGDGVNDAPAMANATVGIAMGAAGSDVALETA</span></span>
<span class="topo-ruler">       610       620       630       640       650       660       670       680  </span>
<span class="topo-line"><span class="topo-outside">DIALMADDLQTLPFAVGLSRKTSRIIRL</span><span class="topo-membrane">NLWFSLGVVALLIPATLFGL</span><span class="topo-inside">G</span><span class="topo-membrane">IGPAVLVHEGSTLVVVANALR</span><span class="topo-outside">LLAFKDNR</span><span class="topo-unknown">VKSA</span></span>
<details class="topo-details"><summary>Topology coordinates (19 regions)</summary>
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
      <td>40</td>
      <td>1</td>
      <td>40</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>41</td>
      <td>43</td>
      <td>41</td>
      <td>43</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>60</td>
      <td>44</td>
      <td>60</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>61</td>
      <td>70</td>
      <td>61</td>
      <td>70</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>71</td>
      <td>91</td>
      <td>71</td>
      <td>91</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>92</td>
      <td>99</td>
      <td>92</td>
      <td>99</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>100</td>
      <td>117</td>
      <td>100</td>
      <td>117</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>118</td>
      <td>118</td>
      <td>118</td>
      <td>118</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>119</td>
      <td>133</td>
      <td>119</td>
      <td>133</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>134</td>
      <td>287</td>
      <td>134</td>
      <td>287</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>288</td>
      <td>306</td>
      <td>288</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>307</td>
      <td>311</td>
      <td>307</td>
      <td>311</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>312</td>
      <td>332</td>
      <td>312</td>
      <td>332</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>333</td>
      <td>628</td>
      <td>333</td>
      <td>628</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>629</td>
      <td>648</td>
      <td>629</td>
      <td>648</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>649</td>
      <td>649</td>
      <td>649</td>
      <td>649</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>650</td>
      <td>670</td>
      <td>650</td>
      <td>670</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>671</td>
      <td>678</td>
      <td>671</td>
      <td>678</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>679</td>
      <td>682</td>
      <td>679</td>
      <td>682</td>
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

### Architecture of PIB-4-ATPases - no classical HMBDs

The sCoaT structures reveal that PIB-4-ATPases possess eight transmembrane
helices (MA, MB followed by M1-M6) and lack classical heavy-metal-binding
domains (HMBDs). Only the first 47 residues remain unmodelled, shorter than
a classical MBD (70 aa). The N-terminal tail is rich in metal-binding residues
(Met, Cys, His, Asp, Glu) but deletion of the first 33 residues shows only
minor effects on catalytic activity in vitro, suggesting this level of
regulation is absent in many PIB-4-ATPases.

### Internal counterion mechanism via conserved histidine H657

A conserved histidine (H657) of the HEGxT motif in M6 serves as a built-in
counterion in PIB-4-ATPases, analogous to K693 in PIB-2-ATPases (SsZntA).
After ion release, H657 shifts to a sandwiched position between S325 and
C327 (SPC motif of M4), preventing back-transfer of the released ion and
allowing completion of the reaction cycle. This represents a unique internal
counterion principle for the PIB-4 subclass.

### Ion release pathway and mechanism

Ion release from the high-affinity binding site is likely initiated by E658
(M6) rotating away from the ion-binding configuration during E1P to E2P
transition, lowering cargo affinity. Subsequently, E120 (M2) serves as a
transient metal ligand along the exit pathway (lined by M2, M4, M5, M6),
stimulating release from the SPC motif. The two determined structures (E2P*
and E2.Pi) are surprisingly similar, suggesting that sCoaT preorganizes
for dephosphorylation already in a late E2P state, similar to LMCA1.

### Potassium-independent turnover in PIB-ATPases

While classical P-type ATPases require K+ for E2P dephosphorylation,
PIB-ATPases are K+-independent. The A-/P-domain linker in sCoaT is
maintained by a direct interaction between R273 (A-domain) and D601
(P-domain), rather than through a K+ ion. Mutation of these residues
(R273A, D601A, D601K) resulted in marked reduction of turnover,
indicating that PIB-ATPases rely on this particularly tight,
ion-independent stabilization more than classical P-type ATPases.

### Novel inhibitors with antimycobacterial activity

A screen of 20,000 compounds identified two novel inhibitors of sCoaT
that block both PIB-2 and PIB-4 ATPase activity, likely by targeting
the shared release pathway. The inhibitors show activity against
Mycobacterium bovis BCG (MIC90 of 18.75 uM for inhibitor 1), with
limited cytotoxicity toward primary human macrophages. Since PIB-ATPases
function as virulence factors in pathogens and are absent in humans,
they represent potential targets for novel antibiotics.

### Type I crystal packing with unrestrained TM domains

The sCoaT crystals exhibit type I crystal packing with minimal contacts
between adjacent membrane-spanning regions. Crystal forming interactions
likely occur through lipid-detergent molecules rather than direct
protein-protein contacts in the transmembrane region. To the authors'
knowledge, this is the first time type I crystals with unrestrained
transmembrane domains have been reported for a P-type ATPase.


## Cross-References

- <a href="/xray-mp-wiki/concepts/protein-families/p-type-atpase/">P-type ATPase Family</a> — sCoaT belongs to the P1B-type (heavy metal transporting) ATPase subfamily
- <a href="/xray-mp-wiki/concepts/enzyme-mechanisms/p-type-atpase-mechanism/">P-type ATPase Mechanism</a> — sCoaT follows the Post-Albers reaction cycle of P-type ATPases
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/ion-release-pathway/">Ion Release Pathway</a> — Paper describes ion release pathway for PIB-4-ATPases via M2, M4, M5, M6
- <a href="/xray-mp-wiki/methods/crystallization/hilide-crystallization/">HiLiDe Crystallization</a> — Method used for structure determination
- <a href="/xray-mp-wiki/proteins/pumps-atpases/ss-znta/">SsZntA (Shigella sonnei Zn2+-ATPase)</a> — SsZntA was used as molecular replacement search model; related PIB-ATPase
- <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM (n-Dodecyl-beta-D-Maltopyranoside)</a> — Detergent used for solubilization of membrane protein
- <a href="/xray-mp-wiki/reagents/detergents/c12e8/">C12E8 (Octaethylene Glycol Monododecyl Ether)</a> — Detergent used in purification and crystallization
- <a href="/xray-mp-wiki/methods/structure-determination/molecular-replacement/">Molecular Replacement</a> — Method used for structure determination
