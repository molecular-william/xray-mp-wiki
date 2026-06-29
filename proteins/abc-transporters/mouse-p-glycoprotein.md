---
title: "Mouse P-glycoprotein"
created: 2026-06-11
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [transporter, membrane-protein, xray-crystallography]
sources: [doi/10.1107##s1399004715000978, doi/10.1002##pro.2387, doi/10.1126##science.1168750, doi/10.1126##sciadv.1600001, doi/10.1107##S2052252520005709]
verified: false
---

# Mouse P-glycoprotein

## Overview

Mouse P-glycoprotein (P-gp; ABCB1; Mdr1a) is an ATP-binding cassette (ABC) transporter that functions as a multidrug efflux pump, exporting a wide array of structurally diverse compounds including chemotherapy drugs, antibiotics, and environmental toxins. It shares 87% sequence identity with human P-gp and serves as the primary structural model for understanding P-gp function. The transporter consists of two transmembrane domains (TMDs) and two nucleotide- binding domains (NBDs), forming a large polyspecific drug-binding cavity enriched in aromatic residues.

## Publications

### doi/10.1107##s1399004715000978

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4q9h">4Q9H</a></td>
      <td>3.4 A</td>
      <td>P2_12_12_1</td>
      <td>Mouse P-gp/Mdr1a (ABCB1), reductively methylated, C-terminal His6 tag</td>
      <td>None (drug-free, apo)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4q9i">4Q9I</a></td>
      <td>3.8 A</td>
      <td>P2_12_12_1</td>
      <td>Mouse P-gp/Mdr1a cocrystallized with QZ-Ala</td>
      <td>QZ-Ala (Se-labeled homotrimeric cyclopeptide)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4q9j">4Q9J</a></td>
      <td>3.6 A</td>
      <td>P2_12_12_1</td>
      <td>Mouse P-gp/Mdr1a cocrystallized with QZ-Val</td>
      <td>QZ-Val (Se-labeled homotrimeric cyclopeptide, formerly QZ59-SSS)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4q9k">4Q9K</a></td>
      <td>3.8 A</td>
      <td>P2_12_12_1</td>
      <td>Mouse P-gp/Mdr1a cocrystallized with QZ-Leu</td>
      <td>QZ-Leu (Se-labeled homotrimeric cyclopeptide)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4q9l">4Q9L</a></td>
      <td>3.8 A</td>
      <td>P2_12_12_1</td>
      <td>Mouse P-gp/Mdr1a cocrystallized with QZ-Phe</td>
      <td>QZ-Phe (Se-labeled homotrimeric cyclopeptide)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (mouse P-gp ABCB1a); also in S. cerevisiae and insect cells
- **Construct**: Mouse ABCB1a with N83Q/N87Q/N90Q mutations (deglycosylated) and C-terminal His6 tag; full-length 1276 residues

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
      <td>Cell disruption and membrane fractionation</td>
      <td>--</td>
      <td>--</td>
      <td>P-gp expressed in Pichia pastoris; membranes solubilized in <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
    </tr>
    <tr>
      <td>Ni-NTA <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td>Ni-NTA Superflow</td>
      <td>20 mM HEPES pH 8.0, 100 mM NaCl, 0.2 mM TCEP, 0.04% <a href="/xray-mp-wiki/reagents/detergents/sodium-cholate/">Sodium Cholate</a>, 0.065% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a></td>
      <td>Protein eluted with 200 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> gradient</td>
    </tr>
    <tr>
      <td>Size-exclusion chromatography</td>
      <td>SEC</td>
      <td><a href="/xray-mp-wiki/reagents/additives/superdex-200/">Superdex 200</a> 16/60</td>
      <td>20 mM HEPES pH 7.5, 100 mM NaCl, 0.2 mM TCEP, 0.01% <a href="/xray-mp-wiki/reagents/detergents/sodium-cholate/">Sodium Cholate</a>, 0.035% beta-<a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a></td>
      <td>Followed by reductive methylation (borane dimethylamine/formaldehyde) for crystallography</td>
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
      <td>Reductively methylated P-gp at ~10-12 mg/ml (1:1 protein:mother liquor)</td>
    </tr>
    <tr>
      <td>Reservoir</td>
      <td>0.1 M HEPES pH 7-8, 50 mM <a href="/xray-mp-wiki/reagents/additives/lithium-sulfate/">Lithium Sulfate</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a>, 24-29.5% <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>4°C (277 K)</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>~2 weeks</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Crystals typically appeared after 1-3 days, grew to full size in ~2 weeks. Cryoprotected in reservoir solution with 32% <a href="/xray-mp-wiki/reagents/additives/peg-600/">PEG 600</a>. Typical crystal dimensions ~650 x 400 x 300 um. Data collected at SSRL BL11-1 and CLS 08ID-1 at 100 K. For co-crystals, excess cyclopeptide removed before crystallization.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4q9h">4Q9H</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEK</span><span class="topo-outside">KPAVSVLTMF</span><span class="topo-membrane">RYAGWLDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMM</span><span class="topo-inside">LIFGDMTDSFASVGQVSKQSTQMSEADKRAMFAKLEEEMTTYAYYYTGI</span><span class="topo-membrane">GAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLAAGRQ</span><span class="topo-outside">IHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKIN</span><span class="topo-membrane">E</span></span>
<span class="topo-line"><span class="topo-membrane">GIGDKIGMFFQAMATFFGGFIIGF</span><span class="topo-inside">TRGW</span><span class="topo-membrane">KLTLVILAISPVLGLSAGIWAKIL</span><span class="topo-outside">SSFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGIKKA</span><span class="topo-membrane">ITANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALAFW</span><span class="topo-inside">YGTSLVISKEYSIGQVLTV</span><span class="topo-membrane">FFSVLIGAFSVGQASPNIEAFA</span><span class="topo-outside">NARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLSTKEALDEDV</span><span class="topo-outside">PPASFW</span><span class="topo-unknown">RILKLN</span><span class="topo-outside">STE</span><span class="topo-membrane">WPYFVVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIF</span><span class="topo-inside">SKVVGVFTNGGPPETQRQNSNLFS</span><span class="topo-membrane">LLFLILGIISFITFFLQGFTFGKA</span><span class="topo-outside">GEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKG</span><span class="topo-membrane">ATGSRLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIIS</span><span class="topo-inside">LIYGWQLTLLL</span><span class="topo-membrane">LAIVPIIAIAGVVEMKMLSGQA</span><span class="topo-outside">LKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPY</span><span class="topo-membrane">RNAMKKAHVFGITFSFTQAMMYFSY</span><span class="topo-inside">AACFRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVLLV</span><span class="topo-membrane">FSAIVFGAMAVGQVSSFAPDY</span><span class="topo-outside">AKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQAGA</span><span class="topo-unknown">KRSLEHHHHHH</span></span>
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
      <td>30</td>
      <td>39</td>
      <td>30</td>
      <td>39</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>40</td>
      <td>68</td>
      <td>40</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>117</td>
      <td>69</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>139</td>
      <td>118</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>179</td>
      <td>140</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>204</td>
      <td>180</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>208</td>
      <td>205</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>232</td>
      <td>209</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>288</td>
      <td>233</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>311</td>
      <td>289</td>
      <td>311</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>312</td>
      <td>330</td>
      <td>312</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>626</td>
      <td>353</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>689</td>
      <td>694</td>
      <td>689</td>
      <td>694</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>695</td>
      <td>700</td>
      <td>695</td>
      <td>700</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>701</td>
      <td>703</td>
      <td>701</td>
      <td>703</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>704</td>
      <td>728</td>
      <td>704</td>
      <td>728</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>729</td>
      <td>752</td>
      <td>729</td>
      <td>752</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>753</td>
      <td>776</td>
      <td>753</td>
      <td>776</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>777</td>
      <td>823</td>
      <td>777</td>
      <td>823</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>824</td>
      <td>846</td>
      <td>824</td>
      <td>846</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>847</td>
      <td>857</td>
      <td>847</td>
      <td>857</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>858</td>
      <td>879</td>
      <td>858</td>
      <td>879</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>880</td>
      <td>924</td>
      <td>880</td>
      <td>924</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>925</td>
      <td>949</td>
      <td>925</td>
      <td>949</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>950</td>
      <td>973</td>
      <td>950</td>
      <td>973</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>974</td>
      <td>994</td>
      <td>974</td>
      <td>994</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>995</td>
      <td>1273</td>
      <td>995</td>
      <td>1273</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4q9i">4Q9I</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEK</span><span class="topo-outside">KPAVSVLTMFRYA</span><span class="topo-membrane">GWLDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMML</span><span class="topo-inside">IFGDMTDSFASVGQVSKQSTQMSEADKRAMFAKLEEEMTTYAYYY</span><span class="topo-membrane">TGIGAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLAAGR</span><span class="topo-outside">QIHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKINE</span></span>
<span class="topo-line"><span class="topo-membrane">GIGDKIGMFFQAMATFFGGFIIGF</span><span class="topo-inside">TRGWKL</span><span class="topo-membrane">TLVILAISPVLGLSAGIWAKILS</span><span class="topo-outside">SFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGI</span><span class="topo-membrane">KKAITANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALAF</span><span class="topo-inside">WYGTSLVISKEYSIGQVL</span><span class="topo-membrane">TVFFSVLIGAFSVGQASPNIEAFA</span><span class="topo-outside">NARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLSTKEALDEDVPPA</span><span class="topo-outside">SFWRILKLNSTE</span><span class="topo-membrane">WPYFVVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIF</span><span class="topo-inside">SKVVGVFTNGGPPETQRQNSNLFS</span><span class="topo-membrane">LLFLILGIISFITFFLQGFTFGKA</span><span class="topo-outside">GEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKGA</span><span class="topo-membrane">TGSRLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISLI</span><span class="topo-inside">YGWQ</span><span class="topo-membrane">LTLLLLAIVPIIAIAGVVEMKMLS</span><span class="topo-outside">GQALKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPYRNA</span><span class="topo-membrane">MKKAHVFGITFSFTQAMMYFSYAAC</span><span class="topo-inside">FRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVLL</span><span class="topo-membrane">VFSAIVFGAMAVGQVSSFAP</span><span class="topo-outside">DYAKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQAGAKRSLE</span><span class="topo-unknown">HHHHHH</span></span>
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
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>42</td>
      <td>30</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>69</td>
      <td>43</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>114</td>
      <td>70</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>138</td>
      <td>115</td>
      <td>138</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>139</td>
      <td>180</td>
      <td>139</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>204</td>
      <td>181</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>210</td>
      <td>205</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>233</td>
      <td>211</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>285</td>
      <td>234</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>310</td>
      <td>286</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>328</td>
      <td>311</td>
      <td>328</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>352</td>
      <td>329</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>626</td>
      <td>353</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>691</td>
      <td>627</td>
      <td>691</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>692</td>
      <td>703</td>
      <td>692</td>
      <td>703</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>704</td>
      <td>728</td>
      <td>704</td>
      <td>728</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>729</td>
      <td>752</td>
      <td>729</td>
      <td>752</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>753</td>
      <td>776</td>
      <td>753</td>
      <td>776</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>777</td>
      <td>824</td>
      <td>777</td>
      <td>824</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>825</td>
      <td>848</td>
      <td>825</td>
      <td>848</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>849</td>
      <td>852</td>
      <td>849</td>
      <td>852</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>853</td>
      <td>876</td>
      <td>853</td>
      <td>876</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>877</td>
      <td>927</td>
      <td>877</td>
      <td>927</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>928</td>
      <td>952</td>
      <td>928</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>953</td>
      <td>972</td>
      <td>953</td>
      <td>972</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>973</td>
      <td>992</td>
      <td>973</td>
      <td>992</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>993</td>
      <td>1278</td>
      <td>993</td>
      <td>1278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1279</td>
      <td>1284</td>
      <td>1279</td>
      <td>1284</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4q9j">4Q9J</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEK</span><span class="topo-outside">KPAVS</span><span class="topo-membrane">VLTMFRYAGWLDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMM</span><span class="topo-inside">LIFGDMTDSFASVGQVSKQSTQMSEADKRAMFAKLEEEMTTYAYYYT</span><span class="topo-membrane">GIGAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLAAGRQ</span><span class="topo-outside">IHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKIN</span><span class="topo-membrane">E</span></span>
<span class="topo-line"><span class="topo-membrane">GIGDKIGMFFQAMATFFGGFIIGF</span><span class="topo-inside">TRGW</span><span class="topo-membrane">KLTLVILAISPVLGLSAGIWAKILS</span><span class="topo-outside">SFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGIKKAI</span><span class="topo-membrane">TANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALAFWY</span><span class="topo-inside">GTSLVISKEYSIGQVL</span><span class="topo-membrane">TVFFSVLIGAFSVGQASPNIEAFA</span><span class="topo-outside">NARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLSTKEALDEDV</span><span class="topo-outside">PPASFWRILKLNSTEW</span><span class="topo-membrane">PYFVVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIFS</span><span class="topo-inside">KVVGVFTNGGPPETQRQNSNLF</span><span class="topo-membrane">SLLFLILGIISFITFFLQGFTF</span><span class="topo-outside">GKAGEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKGATG</span><span class="topo-membrane">SRLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISLI</span><span class="topo-inside">YGWQLT</span><span class="topo-membrane">LLLLAIVPIIAIAGVVEMKMLSGQ</span><span class="topo-outside">ALKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPY</span><span class="topo-membrane">RNAMKKAHVFGITFSFTQAMMYFSYAAC</span><span class="topo-inside">FRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVL</span><span class="topo-membrane">LVFSAIVFGAMAVGQVSSFA</span><span class="topo-outside">PDYAKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQAGAKRSLE</span><span class="topo-unknown">HHHHHH</span></span>
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
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>34</td>
      <td>30</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>68</td>
      <td>35</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>115</td>
      <td>69</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>139</td>
      <td>116</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>179</td>
      <td>140</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>204</td>
      <td>180</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>208</td>
      <td>205</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>233</td>
      <td>209</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>289</td>
      <td>234</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>312</td>
      <td>290</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>328</td>
      <td>313</td>
      <td>328</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>352</td>
      <td>329</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>626</td>
      <td>353</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>688</td>
      <td>627</td>
      <td>688</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>689</td>
      <td>704</td>
      <td>689</td>
      <td>704</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>705</td>
      <td>729</td>
      <td>705</td>
      <td>729</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>730</td>
      <td>751</td>
      <td>730</td>
      <td>751</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>752</td>
      <td>773</td>
      <td>752</td>
      <td>773</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>774</td>
      <td>826</td>
      <td>774</td>
      <td>826</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>827</td>
      <td>848</td>
      <td>827</td>
      <td>848</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>849</td>
      <td>854</td>
      <td>849</td>
      <td>854</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>855</td>
      <td>878</td>
      <td>855</td>
      <td>878</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>879</td>
      <td>924</td>
      <td>879</td>
      <td>924</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>925</td>
      <td>952</td>
      <td>925</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>953</td>
      <td>971</td>
      <td>953</td>
      <td>971</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>972</td>
      <td>991</td>
      <td>972</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1278</td>
      <td>992</td>
      <td>1278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1279</td>
      <td>1284</td>
      <td>1279</td>
      <td>1284</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4q9k">4Q9K</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEK</span><span class="topo-outside">KPAVSVLTMFRYAGW</span><span class="topo-membrane">LDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMML</span><span class="topo-inside">IFGDMTDSFASVGQVSKQSTQMSEADKRAMFAKLEEEMTTYAYYY</span><span class="topo-membrane">TGIGAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLA</span><span class="topo-outside">AGRQIHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKINE</span></span>
<span class="topo-line"><span class="topo-outside">GI</span><span class="topo-membrane">GDKIGMFFQAMATFFGGFIIGF</span><span class="topo-inside">TRGWKL</span><span class="topo-membrane">TLVILAISPVLGLSAGIWAKILSSF</span><span class="topo-outside">TDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAK</span><span class="topo-membrane">RLGIKKAITANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALA</span><span class="topo-inside">FWYGTSLVISKEYSIGQVLTV</span><span class="topo-membrane">FFSVLIGAFSVGQASPNIEAF</span><span class="topo-outside">ANARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLSTKEALDEDV</span><span class="topo-outside">PPASFWRIL</span><span class="topo-membrane">KLNSTEWPYFVVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFS</span><span class="topo-inside">VIFSKVVGVFTNGGPPETQRQNSNLFSLLFL</span><span class="topo-membrane">ILGIISFITFFLQGFTFGKAGEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVK</span><span class="topo-membrane">GATGSRLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGII</span><span class="topo-inside">ISLIYGWQLT</span><span class="topo-membrane">LLLLAIVPIIAIAGVVEMKMLS</span><span class="topo-outside">GQALKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPYRNAM</span><span class="topo-membrane">KKAHVFGITFSFTQAMMYFSYAAC</span><span class="topo-inside">FRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVLLV</span><span class="topo-membrane">FSAIVFGAMAVGQVSSFAPDY</span><span class="topo-outside">AKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQAGAKRSLE</span><span class="topo-unknown">HHHHHH</span></span>
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
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>44</td>
      <td>30</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>69</td>
      <td>45</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>114</td>
      <td>70</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>135</td>
      <td>115</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>182</td>
      <td>136</td>
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
      <td>210</td>
      <td>205</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>235</td>
      <td>211</td>
      <td>235</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>236</td>
      <td>281</td>
      <td>236</td>
      <td>281</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>282</td>
      <td>309</td>
      <td>282</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>330</td>
      <td>310</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>351</td>
      <td>331</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>626</td>
      <td>352</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>688</td>
      <td>627</td>
      <td>688</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>689</td>
      <td>697</td>
      <td>689</td>
      <td>697</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>698</td>
      <td>725</td>
      <td>698</td>
      <td>725</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>726</td>
      <td>756</td>
      <td>726</td>
      <td>756</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>757</td>
      <td>780</td>
      <td>757</td>
      <td>780</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>781</td>
      <td>822</td>
      <td>781</td>
      <td>822</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>823</td>
      <td>844</td>
      <td>823</td>
      <td>844</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>845</td>
      <td>854</td>
      <td>845</td>
      <td>854</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>855</td>
      <td>876</td>
      <td>855</td>
      <td>876</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>877</td>
      <td>928</td>
      <td>877</td>
      <td>928</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>952</td>
      <td>929</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>953</td>
      <td>973</td>
      <td>953</td>
      <td>973</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>974</td>
      <td>994</td>
      <td>974</td>
      <td>994</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>995</td>
      <td>1278</td>
      <td>995</td>
      <td>1278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1279</td>
      <td>1284</td>
      <td>1279</td>
      <td>1284</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4q9l">4Q9L</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEK</span><span class="topo-outside">KPAVSVLTMFRYA</span><span class="topo-membrane">GWLDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMM</span><span class="topo-inside">LIFGDMTDSFASVGQVSKQSTQMSEADKRAMFAKLEEEMTTYAYYY</span><span class="topo-membrane">TGIGAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLAA</span><span class="topo-outside">GRQIHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKINE</span></span>
<span class="topo-line"><span class="topo-outside">G</span><span class="topo-membrane">IGDKIGMFFQAMATFFGGFIIGF</span><span class="topo-inside">TRGWKLT</span><span class="topo-membrane">LVILAISPVLGLSAGIWAKILS</span><span class="topo-outside">SFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGI</span><span class="topo-membrane">KKAITANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALA</span><span class="topo-inside">FWYGTSLVISKEYSIGQVLTV</span><span class="topo-membrane">FFSVLIGAFSVGQASPNIEAFA</span><span class="topo-outside">NARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLSTKEALDEDV</span><span class="topo-outside">PPASFWRILKLNSTE</span><span class="topo-membrane">WPYFVVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSV</span><span class="topo-inside">IFSKVVGVFTNGGPPETQRQNSNLFSLL</span><span class="topo-membrane">FLILGIISFITFFLQGFTFGKA</span><span class="topo-outside">GEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKGA</span><span class="topo-membrane">TGSRLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISLI</span><span class="topo-inside">YGWQ</span><span class="topo-membrane">LTLLLLAIVPIIAIAGVVEMKML</span><span class="topo-outside">SGQALKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPYRNAM</span><span class="topo-membrane">KKAHVFGITFSFTQAMMYFSYAAC</span><span class="topo-inside">FRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVLL</span><span class="topo-membrane">VFSAIVFGAMAVGQVSSFA</span><span class="topo-outside">PDYAKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQAGAKRSLE</span><span class="topo-unknown">HHHHHH</span></span>
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
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>42</td>
      <td>30</td>
      <td>42</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>43</td>
      <td>68</td>
      <td>43</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>114</td>
      <td>69</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>136</td>
      <td>115</td>
      <td>136</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>137</td>
      <td>181</td>
      <td>137</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>204</td>
      <td>182</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>211</td>
      <td>205</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>233</td>
      <td>212</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>285</td>
      <td>234</td>
      <td>285</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>286</td>
      <td>309</td>
      <td>286</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>330</td>
      <td>310</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>626</td>
      <td>353</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>688</td>
      <td>627</td>
      <td>688</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>689</td>
      <td>703</td>
      <td>689</td>
      <td>703</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>704</td>
      <td>726</td>
      <td>704</td>
      <td>726</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>727</td>
      <td>754</td>
      <td>727</td>
      <td>754</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>755</td>
      <td>776</td>
      <td>755</td>
      <td>776</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>777</td>
      <td>824</td>
      <td>777</td>
      <td>824</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>825</td>
      <td>848</td>
      <td>825</td>
      <td>848</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>849</td>
      <td>852</td>
      <td>849</td>
      <td>852</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>853</td>
      <td>875</td>
      <td>853</td>
      <td>875</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>876</td>
      <td>928</td>
      <td>876</td>
      <td>928</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>952</td>
      <td>929</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>953</td>
      <td>972</td>
      <td>953</td>
      <td>972</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>973</td>
      <td>991</td>
      <td>973</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1278</td>
      <td>992</td>
      <td>1278</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1279</td>
      <td>1284</td>
      <td>1279</td>
      <td>1284</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1002##pro.2387

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3g5u">3G5U</a></td>
      <td>3.8 A</td>
      <td>C2</td>
      <td>Mouse P-gp (ABCB1a), original structure by MAD phasing</td>
      <td>None (drug-free)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4m1m">4M1M</a></td>
      <td>3.8 A</td>
      <td>C2</td>
      <td>Mouse P-gp, improved model with corrected TM registry</td>
      <td>None (drug-free)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4m2s">4M2S</a></td>
      <td>4.4 A</td>
      <td>C2</td>
      <td>Mouse P-gp cocrystallized with QZ59-RRR</td>
      <td>QZ59-RRR (cyclic hexapeptide, selenium-labeled)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4m2t">4M2T</a></td>
      <td>4.35 A</td>
      <td>C2</td>
      <td>Mouse P-gp cocrystallized with QZ59-SSS</td>
      <td>QZ59-SSS (cyclic hexapeptide, selenium-labeled)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (mouse P-gp ABCB1a); also in S. cerevisiae and insect cells
- **Construct**: Mouse ABCB1a with N83Q/N87Q/N90Q mutations (deglycosylated) and C-terminal His6 tag; full-length 1276 residues

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3g5u">3G5U</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEKKPA</span><span class="topo-outside">VSVLTMFRYAGW</span><span class="topo-membrane">LDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMM</span><span class="topo-inside">LIFGDMTDSFASVGNVSKNSTNMSEADKRAMFAKLEEEMTTYAYY</span><span class="topo-membrane">YTGIGAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFW</span><span class="topo-outside">CLAAGRQIHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKINE</span></span>
<span class="topo-line"><span class="topo-outside">GIG</span><span class="topo-membrane">DKIGMFFQAMATFFGGFIIG</span><span class="topo-inside">FTRGWKLTLVI</span><span class="topo-membrane">LAISPVLGLSAGIWAKILSS</span><span class="topo-outside">FTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGIKKAIT</span><span class="topo-membrane">ANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALAF</span><span class="topo-inside">WYGTSLVISKEYSIGQVLTVF</span><span class="topo-membrane">FSVLIGAFSVGQASPNIE</span><span class="topo-outside">AFANARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLSTKEA</span><span class="topo-outside">LDEDVPPASFW</span><span class="topo-unknown">RILKLNST</span><span class="topo-outside">EWPYF</span><span class="topo-membrane">VVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIF</span><span class="topo-inside">SKVVGVFTNGGPPETQRQNSNLFS</span><span class="topo-membrane">LLFLILGIISFITFFLQGFTF</span><span class="topo-outside">GKAGEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKGATGSR</span><span class="topo-membrane">LAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISL</span><span class="topo-inside">IYGW</span><span class="topo-membrane">QLTLLLLAIVPIIAIAGVVEM</span><span class="topo-outside">KMLSGQALKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPYRNAMKKAH</span><span class="topo-membrane">VFGITFSFTQAMMYFSYAAAF</span><span class="topo-inside">RFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVLL</span><span class="topo-membrane">VFSAIVFGAMAVGQVSSF</span><span class="topo-outside">APDYAKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQA</span><span class="topo-unknown">GAKRSYVHHHHHH</span></span>
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
      <td>32</td>
      <td>1</td>
      <td>32</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>44</td>
      <td>33</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>68</td>
      <td>45</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>113</td>
      <td>69</td>
      <td>113</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>114</td>
      <td>132</td>
      <td>114</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>183</td>
      <td>133</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>203</td>
      <td>184</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>214</td>
      <td>204</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>234</td>
      <td>215</td>
      <td>234</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>235</td>
      <td>290</td>
      <td>235</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>310</td>
      <td>291</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>331</td>
      <td>311</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>349</td>
      <td>332</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>626</td>
      <td>350</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>683</td>
      <td>627</td>
      <td>683</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>684</td>
      <td>694</td>
      <td>684</td>
      <td>694</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>695</td>
      <td>702</td>
      <td>695</td>
      <td>702</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>703</td>
      <td>707</td>
      <td>703</td>
      <td>707</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>708</td>
      <td>728</td>
      <td>708</td>
      <td>728</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>729</td>
      <td>752</td>
      <td>729</td>
      <td>752</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>753</td>
      <td>773</td>
      <td>753</td>
      <td>773</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>774</td>
      <td>828</td>
      <td>774</td>
      <td>828</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>829</td>
      <td>847</td>
      <td>829</td>
      <td>847</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>848</td>
      <td>851</td>
      <td>848</td>
      <td>851</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>852</td>
      <td>872</td>
      <td>852</td>
      <td>872</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>873</td>
      <td>932</td>
      <td>873</td>
      <td>932</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>933</td>
      <td>953</td>
      <td>933</td>
      <td>953</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>954</td>
      <td>972</td>
      <td>954</td>
      <td>972</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>973</td>
      <td>990</td>
      <td>973</td>
      <td>990</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>991</td>
      <td>1271</td>
      <td>991</td>
      <td>1271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1272</td>
      <td>1284</td>
      <td>1272</td>
      <td>1284</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4m1m">4M1M</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEK</span><span class="topo-outside">KPAVS</span><span class="topo-membrane">VLTMFRYAGWLDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMM</span><span class="topo-inside">LIFGDMTDSFASVGQVSKQSTQMSEADKRAMFAKLEEEMTTYAYYYT</span><span class="topo-membrane">GIGAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLAAGRQ</span><span class="topo-outside">IHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKIN</span><span class="topo-membrane">E</span></span>
<span class="topo-line"><span class="topo-membrane">GIGDKIGMFFQAMATFFGGFIIGF</span><span class="topo-inside">TRGWKLT</span><span class="topo-membrane">LVILAISPVLGLSAGIWAKIL</span><span class="topo-outside">SSFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGIKKA</span><span class="topo-membrane">ITANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALA</span><span class="topo-inside">FWYGTSLVISKEYSIGQVLTV</span><span class="topo-membrane">FFSVLIGAFSVGQASPNIEAFA</span><span class="topo-outside">NARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLST</span><span class="topo-outside">KEALDEDVPPASFWRILKLNSTEW</span><span class="topo-membrane">PYFVVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIF</span><span class="topo-inside">SKVVGVFTNGGPPETQRQNSNLFS</span><span class="topo-membrane">LLFLILGIISFITFFLQGFTFG</span><span class="topo-outside">KAGEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKG</span><span class="topo-membrane">ATGSRLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISL</span><span class="topo-inside">IYGWQLT</span><span class="topo-membrane">LLLLAIVPIIAIAGVVEMKMLSGQA</span><span class="topo-outside">LKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPYR</span><span class="topo-membrane">NAMKKAHVFGITFSFTQAMMYFSYAAA</span><span class="topo-inside">FRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVLL</span><span class="topo-membrane">VFSAIVFGAMAVGQVSSFAPDYA</span><span class="topo-outside">KATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQA</span><span class="topo-unknown">GAKRSHHHHHH</span></span>
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
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>34</td>
      <td>30</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>68</td>
      <td>35</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>115</td>
      <td>69</td>
      <td>115</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>116</td>
      <td>139</td>
      <td>116</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>179</td>
      <td>140</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>204</td>
      <td>180</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>211</td>
      <td>205</td>
      <td>211</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>212</td>
      <td>232</td>
      <td>212</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>288</td>
      <td>233</td>
      <td>288</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>289</td>
      <td>309</td>
      <td>289</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>330</td>
      <td>310</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>352</td>
      <td>331</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>626</td>
      <td>353</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>680</td>
      <td>627</td>
      <td>680</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>681</td>
      <td>704</td>
      <td>681</td>
      <td>704</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>705</td>
      <td>728</td>
      <td>705</td>
      <td>728</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>729</td>
      <td>752</td>
      <td>729</td>
      <td>752</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>753</td>
      <td>774</td>
      <td>753</td>
      <td>774</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>775</td>
      <td>823</td>
      <td>775</td>
      <td>823</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>824</td>
      <td>847</td>
      <td>824</td>
      <td>847</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>848</td>
      <td>854</td>
      <td>848</td>
      <td>854</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>855</td>
      <td>879</td>
      <td>855</td>
      <td>879</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>880</td>
      <td>925</td>
      <td>880</td>
      <td>925</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>926</td>
      <td>952</td>
      <td>926</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>953</td>
      <td>972</td>
      <td>953</td>
      <td>972</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>973</td>
      <td>995</td>
      <td>973</td>
      <td>995</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>996</td>
      <td>1271</td>
      <td>996</td>
      <td>1271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1272</td>
      <td>1282</td>
      <td>1272</td>
      <td>1282</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4m2s">4M2S</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEK</span><span class="topo-outside">KPAVSVLTM</span><span class="topo-membrane">FRYAGWLDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMM</span><span class="topo-inside">LIFGDMTDSFASVGQVSKQSTQMSEADKRAMFAKLEEEMTTYAYYYTGI</span><span class="topo-membrane">GAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLAAGRQ</span><span class="topo-outside">IHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKINE</span></span>
<span class="topo-line"><span class="topo-membrane">GIGDKIGMFFQAMATFFGGFIIGF</span><span class="topo-inside">TRGWKL</span><span class="topo-membrane">TLVILAISPVLGLSAGIWAK</span><span class="topo-outside">ILSSFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGIKKAI</span><span class="topo-membrane">TANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALAFWY</span><span class="topo-inside">GTSLVISKEYSIGQVLT</span><span class="topo-membrane">VFFSVLIGAFSVGQASPNIEAFA</span><span class="topo-outside">NARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLST</span><span class="topo-outside">KEALDEDVPPASFWRILKLNSTEWP</span><span class="topo-membrane">YFVVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIF</span><span class="topo-inside">SKVVGVFTNGGPPETQRQNSNLF</span><span class="topo-membrane">SLLFLILGIISFITFFLQGFTF</span><span class="topo-outside">GKAGEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKGATG</span><span class="topo-membrane">SRLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISL</span><span class="topo-inside">IYGWQLT</span><span class="topo-membrane">LLLLAIVPIIAIAGVVEMKMLSGQA</span><span class="topo-outside">LKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPYR</span><span class="topo-membrane">NAMKKAHVFGITFSFTQAMMYFSYA</span><span class="topo-inside">ACFRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVLL</span><span class="topo-membrane">VFSAIVFGAMAVGQVSSFAPDY</span><span class="topo-outside">AKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQA</span><span class="topo-unknown">GAKRSHHHHHH</span></span>
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
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>38</td>
      <td>30</td>
      <td>38</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>39</td>
      <td>68</td>
      <td>39</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>117</td>
      <td>69</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>139</td>
      <td>118</td>
      <td>139</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>140</td>
      <td>180</td>
      <td>140</td>
      <td>180</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>204</td>
      <td>181</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>210</td>
      <td>205</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>230</td>
      <td>211</td>
      <td>230</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>231</td>
      <td>289</td>
      <td>231</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>312</td>
      <td>290</td>
      <td>312</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>313</td>
      <td>329</td>
      <td>313</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>352</td>
      <td>330</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>626</td>
      <td>353</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>680</td>
      <td>627</td>
      <td>680</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>681</td>
      <td>705</td>
      <td>681</td>
      <td>705</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>706</td>
      <td>728</td>
      <td>706</td>
      <td>728</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>729</td>
      <td>751</td>
      <td>729</td>
      <td>751</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>752</td>
      <td>773</td>
      <td>752</td>
      <td>773</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>774</td>
      <td>826</td>
      <td>774</td>
      <td>826</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>827</td>
      <td>847</td>
      <td>827</td>
      <td>847</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>848</td>
      <td>854</td>
      <td>848</td>
      <td>854</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>855</td>
      <td>879</td>
      <td>855</td>
      <td>879</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>880</td>
      <td>925</td>
      <td>880</td>
      <td>925</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>926</td>
      <td>950</td>
      <td>926</td>
      <td>950</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>951</td>
      <td>972</td>
      <td>951</td>
      <td>972</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>973</td>
      <td>994</td>
      <td>973</td>
      <td>994</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>995</td>
      <td>1271</td>
      <td>995</td>
      <td>1271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1272</td>
      <td>1282</td>
      <td>1272</td>
      <td>1282</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4m2t">4M2T</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEK</span><span class="topo-outside">KPAVSVLTMFRYAGW</span><span class="topo-membrane">LDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMML</span><span class="topo-inside">IFGDMTDSFASVGQVSKQSTQMSEADKRAMFAKLEEEMTTYAYYY</span><span class="topo-membrane">TGIGAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLA</span><span class="topo-outside">AGRQIHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKINE</span></span>
<span class="topo-line"><span class="topo-outside">G</span><span class="topo-membrane">IGDKIGMFFQAMATFFGGFIIGF</span><span class="topo-inside">TRGWKL</span><span class="topo-membrane">TLVILAISPVLGLSAGIWAKIL</span><span class="topo-outside">SSFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGIK</span><span class="topo-membrane">KAITANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALA</span><span class="topo-inside">FWYGTSLVISKEYSIGQVLT</span><span class="topo-membrane">VFFSVLIGAFSVGQASPNIEAF</span><span class="topo-outside">ANARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLST</span><span class="topo-outside">KEALDEDVPPASFWRILKLNSTE</span><span class="topo-membrane">WPYFVVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIF</span><span class="topo-inside">SKVVGVFTNGGPPETQRQNSNLFSL</span><span class="topo-membrane">LFLILGIISFITFFLQGFTFGKA</span><span class="topo-outside">GEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKG</span><span class="topo-membrane">ATGSRLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISL</span><span class="topo-inside">IYGWQLT</span><span class="topo-membrane">LLLLAIVPIIAIAGVVEMKML</span><span class="topo-outside">SGQALKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPYRNAM</span><span class="topo-membrane">KKAHVFGITFSFTQAMMYFSYAAC</span><span class="topo-inside">FRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVLLV</span><span class="topo-membrane">FSAIVFGAMAVGQVSSFAPDY</span><span class="topo-outside">AKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQA</span><span class="topo-unknown">GAKRSHHHHHH</span></span>
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
      <td>29</td>
      <td>1</td>
      <td>29</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>30</td>
      <td>44</td>
      <td>30</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>69</td>
      <td>45</td>
      <td>69</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>70</td>
      <td>114</td>
      <td>70</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>135</td>
      <td>115</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>181</td>
      <td>136</td>
      <td>181</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>182</td>
      <td>204</td>
      <td>182</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>210</td>
      <td>205</td>
      <td>210</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>211</td>
      <td>232</td>
      <td>211</td>
      <td>232</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>233</td>
      <td>286</td>
      <td>233</td>
      <td>286</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>287</td>
      <td>309</td>
      <td>287</td>
      <td>309</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>310</td>
      <td>329</td>
      <td>310</td>
      <td>329</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>330</td>
      <td>351</td>
      <td>330</td>
      <td>351</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>352</td>
      <td>626</td>
      <td>352</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>680</td>
      <td>627</td>
      <td>680</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>681</td>
      <td>703</td>
      <td>681</td>
      <td>703</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>704</td>
      <td>728</td>
      <td>704</td>
      <td>728</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>729</td>
      <td>753</td>
      <td>729</td>
      <td>753</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>754</td>
      <td>776</td>
      <td>754</td>
      <td>776</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>777</td>
      <td>823</td>
      <td>777</td>
      <td>823</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>824</td>
      <td>847</td>
      <td>824</td>
      <td>847</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>848</td>
      <td>854</td>
      <td>848</td>
      <td>854</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>855</td>
      <td>875</td>
      <td>855</td>
      <td>875</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>876</td>
      <td>928</td>
      <td>876</td>
      <td>928</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>929</td>
      <td>952</td>
      <td>929</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>953</td>
      <td>973</td>
      <td>953</td>
      <td>973</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>974</td>
      <td>994</td>
      <td>974</td>
      <td>994</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>995</td>
      <td>1271</td>
      <td>995</td>
      <td>1271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1272</td>
      <td>1282</td>
      <td>1272</td>
      <td>1282</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1126##science.1168750

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3gsu">3GSU</a></td>
      <td>3.8 A</td>
      <td>C2</td>
      <td>Mouse P-gp (ABCB1a), drug-free inward-facing conformation</td>
      <td>None (drug-free)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3g60">3G60</a></td>
      <td>4.4 A</td>
      <td>C2</td>
      <td>Mouse P-gp cocrystallized with QZ59-RRR</td>
      <td>QZ59-RRR (cyclic hexapeptide)</td>
    </tr>
    <tr>
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/3g61">3G61</a></td>
      <td>4.35 A</td>
      <td>C2</td>
      <td>Mouse P-gp cocrystallized with QZ59-SSS</td>
      <td>QZ59-SSS (cyclic hexapeptide)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (mouse P-gp ABCB1a); also in S. cerevisiae and insect cells
- **Construct**: Mouse ABCB1a with N83Q/N87Q/N90Q mutations (deglycosylated) and C-terminal His6 tag; full-length 1276 residues

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3g60">3G60</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEKKPA</span><span class="topo-outside">V</span><span class="topo-unknown">SVLTMF</span><span class="topo-outside">RYAGW</span><span class="topo-membrane">LDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMM</span><span class="topo-inside">LIFGDMTDSFASVGNVSKNSTNMSEADKRAMFAKLEEEMTTYAYYY</span><span class="topo-membrane">TGIGAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLA</span><span class="topo-outside">AGRQIHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKINE</span></span>
<span class="topo-line"><span class="topo-outside">GIG</span><span class="topo-membrane">DKIGMFFQAMATFFGGFIIG</span><span class="topo-inside">FTRGWKLTLVI</span><span class="topo-membrane">LAISPVLGLSAGIWAKILS</span><span class="topo-outside">SFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGIKKAIT</span><span class="topo-membrane">ANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALAF</span><span class="topo-inside">WYGTSLVISKEYSIGQVLTV</span><span class="topo-membrane">FFSVLIGAFSVGQASPNIE</span><span class="topo-outside">AFANARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLSTKEA</span><span class="topo-outside">LDEDVPPASFW</span><span class="topo-unknown">RILKLNST</span><span class="topo-outside">EWPYF</span><span class="topo-membrane">VVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIF</span><span class="topo-inside">SKVVGVFTNGGPPETQRQNSNLFS</span><span class="topo-membrane">LLFLILGIISFITFFLQGFTF</span><span class="topo-outside">GKAGEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKGATGSR</span><span class="topo-membrane">LAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISL</span><span class="topo-inside">IYGWQL</span><span class="topo-membrane">TLLLLAIVPIIAIAGVVEM</span><span class="topo-outside">KMLSGQALKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPYRNAMKKA</span><span class="topo-membrane">HVFGITFSFTQAMMYFSYAAC</span><span class="topo-inside">FRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVL</span><span class="topo-membrane">LVFSAIVFGAMAVGQVSSF</span><span class="topo-outside">APDYAKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQA</span><span class="topo-unknown">GAKRSYVHHHHHH</span></span>
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
      <td>32</td>
      <td>1</td>
      <td>32</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>33</td>
      <td>33</td>
      <td>33</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>34</td>
      <td>39</td>
      <td>34</td>
      <td>39</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>40</td>
      <td>44</td>
      <td>40</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>68</td>
      <td>45</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>114</td>
      <td>69</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>135</td>
      <td>115</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>136</td>
      <td>183</td>
      <td>136</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>203</td>
      <td>184</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>214</td>
      <td>204</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>233</td>
      <td>215</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>290</td>
      <td>234</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>310</td>
      <td>291</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>330</td>
      <td>311</td>
      <td>330</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>331</td>
      <td>349</td>
      <td>331</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>626</td>
      <td>350</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>683</td>
      <td>627</td>
      <td>683</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>684</td>
      <td>694</td>
      <td>684</td>
      <td>694</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>695</td>
      <td>702</td>
      <td>695</td>
      <td>702</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>703</td>
      <td>707</td>
      <td>703</td>
      <td>707</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>708</td>
      <td>728</td>
      <td>708</td>
      <td>728</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>729</td>
      <td>752</td>
      <td>729</td>
      <td>752</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>753</td>
      <td>773</td>
      <td>753</td>
      <td>773</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>774</td>
      <td>828</td>
      <td>774</td>
      <td>828</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>829</td>
      <td>847</td>
      <td>829</td>
      <td>847</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>848</td>
      <td>853</td>
      <td>848</td>
      <td>853</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>854</td>
      <td>872</td>
      <td>854</td>
      <td>872</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>873</td>
      <td>931</td>
      <td>873</td>
      <td>931</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>932</td>
      <td>952</td>
      <td>932</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>953</td>
      <td>971</td>
      <td>953</td>
      <td>971</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>972</td>
      <td>990</td>
      <td>972</td>
      <td>990</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>991</td>
      <td>1271</td>
      <td>991</td>
      <td>1271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1272</td>
      <td>1284</td>
      <td>1272</td>
      <td>1284</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/3g61">3G61</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEKKPA</span><span class="topo-outside">VSVLTMFRYAGW</span><span class="topo-membrane">LDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMM</span><span class="topo-inside">LIFGDMTDSFASVGNVSKNSTNMSEADKRAMFAKLEEEMTTYAYYY</span><span class="topo-membrane">TGIGAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFW</span><span class="topo-outside">CLAAGRQIHKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKINE</span></span>
<span class="topo-line"><span class="topo-outside">GIG</span><span class="topo-membrane">DKIGMFFQAMATFFGGFIIG</span><span class="topo-inside">FTRGWKLTLVI</span><span class="topo-membrane">LAISPVLGLSAGIWAKILS</span><span class="topo-outside">SFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGIKKAIT</span><span class="topo-membrane">ANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALAF</span><span class="topo-inside">WYGTSLVISKEYSIGQVLTVF</span><span class="topo-membrane">FSVLIGAFSVGQASPNIE</span><span class="topo-outside">AFANARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLSTKEA</span><span class="topo-outside">LDEDVPPASFW</span><span class="topo-unknown">RILKLNSTE</span><span class="topo-outside">WPYF</span><span class="topo-membrane">VVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIF</span><span class="topo-inside">SKVVGVFTNGGPPETQRQNSNLFSL</span><span class="topo-membrane">LFLILGIISFITFFLQGFTF</span><span class="topo-outside">GKAGEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKGATGS</span><span class="topo-membrane">RLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISL</span><span class="topo-inside">IYGWQL</span><span class="topo-membrane">TLLLLAIVPIIAIAGVVEM</span><span class="topo-outside">KMLSGQALKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPYRNAMKKA</span><span class="topo-membrane">HVFGITFSFTQAMMYFSYAAC</span><span class="topo-inside">FRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVLL</span><span class="topo-membrane">VFSAIVFGAMAVGQVSSF</span><span class="topo-outside">APDYAKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQA</span><span class="topo-unknown">GAKRSYVHHHHHH</span></span>
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
      <td>32</td>
      <td>1</td>
      <td>32</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>33</td>
      <td>44</td>
      <td>33</td>
      <td>44</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>45</td>
      <td>68</td>
      <td>45</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>114</td>
      <td>69</td>
      <td>114</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>115</td>
      <td>132</td>
      <td>115</td>
      <td>132</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>133</td>
      <td>183</td>
      <td>133</td>
      <td>183</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>184</td>
      <td>203</td>
      <td>184</td>
      <td>203</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>204</td>
      <td>214</td>
      <td>204</td>
      <td>214</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>215</td>
      <td>233</td>
      <td>215</td>
      <td>233</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>234</td>
      <td>290</td>
      <td>234</td>
      <td>290</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>291</td>
      <td>310</td>
      <td>291</td>
      <td>310</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>311</td>
      <td>331</td>
      <td>311</td>
      <td>331</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>332</td>
      <td>349</td>
      <td>332</td>
      <td>349</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>350</td>
      <td>626</td>
      <td>350</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>627</td>
      <td>683</td>
      <td>627</td>
      <td>683</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>684</td>
      <td>694</td>
      <td>684</td>
      <td>694</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>695</td>
      <td>703</td>
      <td>695</td>
      <td>703</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>704</td>
      <td>707</td>
      <td>704</td>
      <td>707</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>708</td>
      <td>728</td>
      <td>708</td>
      <td>728</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>729</td>
      <td>753</td>
      <td>729</td>
      <td>753</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>754</td>
      <td>773</td>
      <td>754</td>
      <td>773</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>774</td>
      <td>827</td>
      <td>774</td>
      <td>827</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>828</td>
      <td>847</td>
      <td>828</td>
      <td>847</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>848</td>
      <td>853</td>
      <td>848</td>
      <td>853</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>854</td>
      <td>872</td>
      <td>854</td>
      <td>872</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>873</td>
      <td>931</td>
      <td>873</td>
      <td>931</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>932</td>
      <td>952</td>
      <td>932</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>953</td>
      <td>972</td>
      <td>953</td>
      <td>972</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>973</td>
      <td>990</td>
      <td>973</td>
      <td>990</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>991</td>
      <td>1271</td>
      <td>991</td>
      <td>1271</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>1272</td>
      <td>1284</td>
      <td>1272</td>
      <td>1284</td>
      <td>Unknown</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1126##sciadv.1600001

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/4xwk">4XWK</a></td>
      <td>3.5 A</td>
      <td>P2_12_12_1</td>
      <td>Mouse P-gp N83Q/N87Q/N90Q mutant, expressed in P. pastoris</td>
      <td>PBDE-100</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (mouse P-gp ABCB1a); also in S. cerevisiae and insect cells
- **Construct**: Mouse ABCB1a with N83Q/N87Q/N90Q mutations (deglycosylated) and C-terminal His6 tag; full-length 1276 residues

<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/4xwk">4XWK</a> — Chain A (12 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-line"><span class="topo-unknown">MELEEDLKGRADKNFSKMGKKSKKEKKEK</span><span class="topo-outside">KPAVS</span><span class="topo-membrane">VLTMFRYAGWLDRLYMLVGTLAAIIH</span></span>
<span class="topo-line"><span class="topo-membrane">GVALPLMM</span><span class="topo-inside">LIFGDMTDSFASVGQVSKQSTQMSEADKRAMFAKLEEEMTTYAYYYTGI</span><span class="topo-membrane">GAG</span></span>
<span class="topo-line"><span class="topo-membrane">VLIVAYIQVSFWCLAAGRQI</span><span class="topo-outside">HKIRQKFFHAIMNQEIGWFDVHDVGELNTRLTDDVSKIN</span><span class="topo-membrane">E</span></span>
<span class="topo-line"><span class="topo-membrane">GIGDKIGMFFQAMATFFGGFIIGF</span><span class="topo-inside">TRGW</span><span class="topo-membrane">KLTLVILAISPVLGLSAGIWA</span><span class="topo-outside">KILSSFTDKEL</span></span>
<span class="topo-line"><span class="topo-outside">HAYAKAGAVAEEVLAAIRTVIAFGGQKKELERYNNNLEEAKRLGIKKAI</span><span class="topo-membrane">TANISMGAAFL</span></span>
<span class="topo-line"><span class="topo-membrane">LIYASYALAFWYG</span><span class="topo-inside">TSLVISKEYSIGQVL</span><span class="topo-membrane">TVFFSVLIGAFSVGQASPNIEAFA</span><span class="topo-outside">NARGAAYE</span></span>
<span class="topo-line"><span class="topo-outside">VFKIIDNKPSIDSFSKSGHKPDNIQGNLEFKNIHFSYPSRKEVQILKGLNLKVKSGQTVA</span></span>
<span class="topo-line"><span class="topo-outside">LVGNSGCGKSTTVQLMQRLYDPLDGMVSIDGQDIRTINVRYLREIIGVVSQEPVLFATTI</span></span>
<span class="topo-line"><span class="topo-outside">AENIRYGREDVTMDEIEKAVKEANAYDFIMKLPHQFDTLVGERGAQLSGGQKQRIAIARA</span></span>
<span class="topo-line"><span class="topo-outside">LVRNPKILLLDEATSALDTESEAVVQAALDKAREGRTTIVIAHRLSTVRNADVIAGFDGG</span></span>
<span class="topo-line"><span class="topo-outside">VIVEQGNHDELMREKGIYFKLVMTQT</span><span class="topo-unknown">AGNEIELGNEACKSKDEIDNLDMSSKDSGSSLIR</span></span>
<span class="topo-line"><span class="topo-unknown">RRSTRKSICGPHDQDRKLSTKEALDEDV</span><span class="topo-outside">PPASFW</span><span class="topo-unknown">RILKLN</span><span class="topo-outside">STEWP</span><span class="topo-membrane">YFVVGIFCAIINGGL</span></span>
<span class="topo-line"><span class="topo-membrane">QPAFSVIFS</span><span class="topo-inside">KVVGVFTNGGPPETQRQNSNL</span><span class="topo-membrane">FSLLFLILGIISFITFFLQGFTF</span><span class="topo-outside">GKAGEIL</span></span>
<span class="topo-line"><span class="topo-outside">TKRLRYMVFKSMLRQDVSWFDDPKNTTGALTTRLANDAAQVKGATGS</span><span class="topo-membrane">RLAVIFQNIANLG</span></span>
<span class="topo-line"><span class="topo-membrane">TGIIISLI</span><span class="topo-inside">YGWQL</span><span class="topo-membrane">TLLLLAIVPIIAIAGVVEMKMLSGQA</span><span class="topo-outside">LKDKKELEGSGKIATEAIENF</span></span>
<span class="topo-line"><span class="topo-outside">RTVVSLTREQKFETMYAQSLQIPY</span><span class="topo-membrane">RNAMKKAHVFGITFSFTQAMMYFSYAAC</span><span class="topo-inside">FRFGAYLV</span></span>
<span class="topo-line"><span class="topo-inside">TQQLMTFENVL</span><span class="topo-membrane">LVFSAIVFGAMAVGQVSSFA</span><span class="topo-outside">PDYAKATVSASHIIRIIEKTPEIDSYSTQ</span></span>
<span class="topo-line"><span class="topo-outside">GLKPNMLEGNVQFSGVVFNYPTRPSIPVLQGLSLEVKKGQTLALVGSSGCGKSTVVQLLE</span></span>
<span class="topo-line"><span class="topo-outside">RFYDPMAGSVFLDGKEIKQLNVQWLRAQLGIVSQEPILFDCSIAENIAYGDNSRVVSYEE</span></span>
<span class="topo-line"><span class="topo-outside">IVRAAKEANIHQFIDSLPDKYNTRVGDKGTQLSGGQKQRIAIARALVRQPHILLLDEATS</span></span>
<span class="topo-line"><span class="topo-outside">ALDTESEKVVQEALDKAREGRTCIVIAHRLSTIQNADLIVVIQNGKVKEHGTHQQLLAQK</span></span>
<span class="topo-line"><span class="topo-outside">GIYFSMVSVQAGA</span><span class="topo-unknown">KRSLEHHHHHH</span></span>
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
      <td>30</td>
      <td>34</td>
      <td>30</td>
      <td>34</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>35</td>
      <td>68</td>
      <td>35</td>
      <td>68</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>69</td>
      <td>117</td>
      <td>69</td>
      <td>117</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>118</td>
      <td>140</td>
      <td>118</td>
      <td>140</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>141</td>
      <td>179</td>
      <td>141</td>
      <td>179</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>180</td>
      <td>204</td>
      <td>180</td>
      <td>204</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>205</td>
      <td>208</td>
      <td>205</td>
      <td>208</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>209</td>
      <td>229</td>
      <td>209</td>
      <td>229</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>230</td>
      <td>289</td>
      <td>230</td>
      <td>289</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>290</td>
      <td>313</td>
      <td>290</td>
      <td>313</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>314</td>
      <td>328</td>
      <td>314</td>
      <td>328</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>329</td>
      <td>352</td>
      <td>329</td>
      <td>352</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>353</td>
      <td>626</td>
      <td>353</td>
      <td>626</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>689</td>
      <td>694</td>
      <td>689</td>
      <td>694</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>695</td>
      <td>700</td>
      <td>695</td>
      <td>700</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>701</td>
      <td>705</td>
      <td>701</td>
      <td>705</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>706</td>
      <td>729</td>
      <td>706</td>
      <td>729</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>730</td>
      <td>750</td>
      <td>730</td>
      <td>750</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>751</td>
      <td>773</td>
      <td>751</td>
      <td>773</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>774</td>
      <td>827</td>
      <td>774</td>
      <td>827</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>828</td>
      <td>848</td>
      <td>828</td>
      <td>848</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>849</td>
      <td>853</td>
      <td>849</td>
      <td>853</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>854</td>
      <td>879</td>
      <td>854</td>
      <td>879</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>880</td>
      <td>924</td>
      <td>880</td>
      <td>924</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>925</td>
      <td>952</td>
      <td>925</td>
      <td>952</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>953</td>
      <td>971</td>
      <td>953</td>
      <td>971</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>972</td>
      <td>991</td>
      <td>972</td>
      <td>991</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>992</td>
      <td>1273</td>
      <td>992</td>
      <td>1273</td>
      <td>Outside</td>
    </tr>
  </tbody>
</table>
</div>
</div>
</div>

</div>
### doi/10.1107##S2052252520005709

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6unj">6UNJ</a></td>
      <td>3.98 A</td>
      <td>P2_12_12_1</td>
      <td>Mouse P-gp C952A mutant (parent control)</td>
      <td><a href="/xray-mp-wiki/reagents/ligands/bde-100/">BDE-100 (2,2',4,4'-Tetrabromodiphenyl Ether)</a></td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Pichia pastoris (mouse P-gp ABCB1a); also in S. cerevisiae and insect cells
- **Construct**: Mouse ABCB1a with N83Q/N87Q/N90Q mutations (deglycosylated) and C-terminal His6 tag; full-length 1276 residues


## Biological / Functional Insights

### TM4 kinking induced by small-molecule ligands

Binding of subset A ligands (QZ-Ala, QZ-Val) induces a large conformational change in TM4, kinking it by up to 11 A at C-alpha positions compared to the straight-helical conformation in apo P-gp and subset B complexes. This kink begins at Pro219 and returns to wild-type topology at Tyr243 near the ball-and- socket region close to NBD2. The movement brings residues 221-228 closer to bound ligands, fostering interaction with Trp228 (implicated in steroid binding). This provides a structural glimpse of the induced-fit model of drug binding in P-gp and suggests a mechanism for transmitting substrate-binding signals from the TMDs to the NBDs.

### EH2 elbow helix as a ligand entry site

A new ligand-binding site was identified on the surface of P-gp facing the inner leaflet of the membrane, involving the elbow helix 2 (EH2, residues 689-694). This site provides vital insights into the entry mechanism of hydrophobic drugs and lipids into P-gp. The EH2 region acts as a portal for substrate entry from the inner leaflet before ligands reach the main drug-binding cavity.

### Multiple binding modes for cyclopeptide substrates

Four homotrimeric cyclopeptide ligands differing only in R-group size (QZ-Ala, QZ-Val, QZ-Leu, QZ-Phe) revealed distinct binding modes. Smaller ligands (subset A: QZ-Ala, QZ-Val) share upper and lower binding sites, while larger ligands (subset B: QZ-Leu, QZ-Phe) bind at a different upper site, with QZ-Phe also occupying a unique lower site. This demonstrates the polyspecific nature of the P-gp binding cavity, accommodating diverse substrates through overlapping but distinct binding subsites.

### Ligand size inversely correlates with ATPase stimulation

QZ-Ala potently stimulated ATP hydrolysis (~16-fold, EC50=0.92 uM), with smaller ligands being more stimulatory. QZ-Val showed ~7-fold stimulation, while QZ-Leu and QZ-Phe were weak stimulators or inhibitors. This correlates with the structural observation that subset A ligands induce TM4 kinking (proposed to transmit a signal to NBDs), while subset B ligands do not. Calcein-AM transport inhibition followed the same trend: QZ-Ala IC50=140 nM, QZ-Val 1.7 uM, QZ-Leu 5.4 uM, QZ-Phe 24 uM.


## Cross-References

- <a href="/xray-mp-wiki/concepts/miscellaneous/p-glycoprotein-induced-fit-binding/">P-glycoprotein Induced-Fit Binding</a> — TM4 kinking provides structural evidence for induced-fit model of drug binding in P-gp
- <a href="/xray-mp-wiki/concepts/transport-mechanisms/abc-transporter-family/">ABC Transporter Family</a> — P-gp is a member of the ABCB/MDR subfamily of ABC transporters
- <a href="/xray-mp-wiki/reagents/ligands/qz-ala/">QZ-Ala</a> — Se-labeled homotrimeric cyclopeptide ATPase stimulator; cocrystal structure determined
- <a href="/xray-mp-wiki/reagents/ligands/qz-val/">QZ-Val</a> — Se-labeled homotrimeric cyclopeptide; cocrystal structure determined
- <a href="/xray-mp-wiki/reagents/ligands/qz-leu/">QZ-Leu</a> — Se-labeled homotrimeric cyclopeptide; cocrystal structure determined
- <a href="/xray-mp-wiki/reagents/ligands/qz-phe/">QZ-Phe</a> — Se-labeled homotrimeric cyclopeptide; cocrystal structure determined
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/additives/edta/">EDTA</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/lithium-sulfate/">Lithium Sulfate</a> — Additive used in purification or crystallization buffers
