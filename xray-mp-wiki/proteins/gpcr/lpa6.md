---
title: "Lysophosphatidic Acid Receptor 6 (LPA6/P2Y5)"
created: 2026-06-16
updated: 2026-07-03
type: protein
category: proteins
layout: default
tags: [gpcr, receptor, membrane-protein, xray-crystallography]
sources: [doi/10.1038##nature23448]
verified: agent
uniprot_id: Q08BG4
---

# Lysophosphatidic Acid Receptor 6 (LPA6/P2Y5)

<div class="expr-badges"><span class="expr-badge expr-sf9">Sf9</span></div>


<a class="badge badge-uniprot" href="https://www.uniprot.org/uniprot/Q08BG4">UniProt: Q08BG4</a>

<span class="expr-badge">Danio rerio</span>

## Overview

Lysophosphatidic acid receptor 6 (LPA6, also known as P2Y5 or LPAR6) is a class A G protein-coupled receptor that belongs to the phylogenetically distant non-EDG family of LPA receptors (LPA4-LPA6). LPA6 is activated by lysophosphatidic acid (LPA), a bioactive lipid composed of a phosphate group, a glycerol backbone, and a single acyl chain. Unlike the EDG family LPA receptors (LPA1-LPA3), the non-EDG family shares sequence similarity with the P2Y family of nucleotide receptors. LPA6 regulates hair follicle formation, and null mutations in LPAR6 or the upstream LPA-producing enzyme PA-PLA1alpha (LIPH) cause autosomal recessive wooly hair/hypotrichosis, a congenital hair disease. LPA6 is also involved in cancer progression. The 3.2 A crystal structure of zebrafish LPA6a revealed a laterally open ligand-binding pocket towards the membrane and provided insights into the LPA recognition mechanism of non-EDG family LPA receptors.

## Publications

### doi/10.1038##nature23448

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/5xsz">5XSZ</a></td>
      <td>3.20</td>
      <td>P2_12_12_1</td>
      <td>Zebrafish LPA6a (Uniprot Q08BG4) with C-terminal truncation (residues 313-357 removed) and T4L insertion in ICL3 between V227 and L233; monoolein-bound; inactive state</td>
      <td>Monoolein (MO1-MO3)</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Sf9 insect cells (Bac-to-Bac baculovirus expression system)
- **Construct**: Zebrafish LPA6a (Uniprot Q08BG4) with N-terminal HA signal + Flag tag + TEV site; C-terminal TEV site + eGFP-His6 tag; C-terminal truncation (residues 313-357 removed); T4L inserted in ICL3 between V227 and L233 for crystallization
- **Notes**: Sf9 cells infected at 3 x 10^5 cells/mL, incubated 48 h at 27 C. Cells collected by centrifugation, resuspended in 50 mM Na-citrate pH 5.0, 150 mM NaCl, 10% glycerol with protease inhibitors.

**Purification:**

- **Expression system**: Sf9 insect cells
- **Expression construct**: Zebrafish LPA6a with N-term HA-Flag-TEV and C-term TEV-eGFP-His6 tags; C-terminal truncation (313-357); T4L fusion in ICL3
- **Tag info**: HA signal + Flag epitope (N-term), eGFP-His6 tag (C-term)

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
      <td>Sonication</td>
      <td></td>
      <td>50 mM Na-<a href="/xray-mp-wiki/reagents/buffers/citrate/">citrate</a> pH 5.0, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>, 1.0 ug/mL aprotinin, 0.4 ug/mL leupeptin</td>
      <td>Cells disrupted by sonication; membrane fraction collected by ultracentrifugation at 125,000g for 1 h at 4 C</td>
    </tr>
    <tr>
      <td>Membrane solubilization</td>
      <td>Detergent solubilization</td>
      <td></td>
      <td>50 mM Na-<a href="/xray-mp-wiki/reagents/buffers/citrate/">citrate</a> pH 5.0, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>, 1.0 ug/mL aprotinin, 0.4 ug/mL leupeptin, 2 mg/mL <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">iodoacetamide</a> + 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Solubilization for 2 h at 4 C; insoluble material removed by ultracentrifugation at 125,000g for 30 min</td>
    </tr>
    <tr>
      <td>Ni Sepharose affinity chromatography</td>
      <td>Immobilized metal <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">affinity chromatography</a></td>
      <td>Ni Sepharose excel resin (GE Healthcare)</td>
      <td>50 mM Na-<a href="/xray-mp-wiki/reagents/buffers/citrate/">citrate</a> pH 5.0, 150 mM NaCl, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">glycerol</a>, 0.1 mM <a href="/xray-mp-wiki/reagents/additives/pmsf/">PMSF</a>, 1.0 ug/mL aprotinin, 0.4 ug/mL leupeptin, 20 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a> + 0.1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.02% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">[CHS</a>](/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/)</td>
      <td>Batch incubation for 1.5 h at 4 C; washed with 10 column volumes; eluted with 300 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">imidazole</a></td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td><a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">Lipidic cubic phase</a> (LCP) crystallization</td>
    </tr>
    <tr>
      <td>Protein sample</td>
      <td>Purified <a href="/xray-mp-wiki/proteins/lpa6/">LPA6</a>-<a href="/xray-mp-wiki/reagents/protein-tags/t4-lysozyme/">T4L</a> fusion protein (after TEV cleavage to remove eGFP-<a href="/xray-mp-wiki/reagents/protein-tags/his6-tag/">His6 tag</a>)</td>
    </tr>
    <tr>
      <td>Lipid</td>
      <td><a href="/xray-mp-wiki/reagents/lipids/monoolein">Monoolein</a> (90% w/w) + <a href="/xray-mp-wiki/reagents/lipids/cholesterol">Cholesterol</a> (10% w/w)</td>
    </tr>
    <tr>
      <td>Protein-to-lipid ratio</td>
      <td>2:3 (protein:lipid)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>20 C</td>
    </tr>
    <tr>
      <td>Growth time</td>
      <td>3-4 wk</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>241 crystals merged into single dataset for 3.2 A resolution structure. Data collected at SPring-8 BL32XU beamline using 10 um minibeam. Rastering used to find best diffracting crystal regions.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/5xsz">5XSZ</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-unknown">GMYNTSLEMEMLNVSNVTHCPKN</span><span class="topo-inside">DNFKYPLYS</span><span class="topo-membrane">MVFSIVFMVGLITNVAAMYIFMCS</span><span class="topo-outside">LKLRN</span><span class="topo-membrane">ETTTYMMNLVVSDLLFVLTLP</span><span class="topo-inside">LRVFYFVQQNWPFGSLLCKLSV</span><span class="topo-membrane">SLFYTNMYGSILFLTC</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-membrane">ISVDRF</span><span class="topo-outside">LAIVYPFRSRGL</span><span class="topo-membrane">RTKRNAKIVCAAVWVLVLSGSLP</span><span class="topo-inside">TGFMLNSTNKLENNSISCF</span><span class="topo-unknown">ENFSSK</span><span class="topo-inside">EWKSHLSK</span><span class="topo-membrane">VVIFIETVGFLIPLMLNVVCSAM</span><span class="topo-outside">VLQTLRRPNTVNIFEMLRIDNGL</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-outside">RLKIYKNTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNTNGVITKDEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRAALINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNL</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       </span>
<span class="topo-line"><span class="topo-outside">AKSRWYNQTPNRAKRVITTFRTGTWDAYLNKKKIL</span><span class="topo-membrane">RMIIVHLFIFCFCFIPYNVNLVF</span><span class="topo-inside">YSLVRTNTLKGCAAESVVRT</span><span class="topo-membrane">IYPIALCIAVSNCCFDPIVYYFTS</span><span class="topo-outside">ETIQNSASSEDLYFQ</span></span>
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
      <td>23</td>
      <td>0</td>
      <td>22</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>24</td>
      <td>32</td>
      <td>23</td>
      <td>31</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>33</td>
      <td>56</td>
      <td>32</td>
      <td>55</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>57</td>
      <td>61</td>
      <td>56</td>
      <td>60</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>62</td>
      <td>82</td>
      <td>61</td>
      <td>81</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>83</td>
      <td>104</td>
      <td>82</td>
      <td>103</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>105</td>
      <td>126</td>
      <td>104</td>
      <td>125</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>127</td>
      <td>138</td>
      <td>126</td>
      <td>137</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>139</td>
      <td>161</td>
      <td>138</td>
      <td>160</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>162</td>
      <td>180</td>
      <td>161</td>
      <td>179</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>181</td>
      <td>186</td>
      <td>180</td>
      <td>185</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>187</td>
      <td>194</td>
      <td>186</td>
      <td>193</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>195</td>
      <td>217</td>
      <td>194</td>
      <td>216</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>218</td>
      <td>395</td>
      <td>217</td>
      <td>239</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>396</td>
      <td>418</td>
      <td>240</td>
      <td>262</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>419</td>
      <td>438</td>
      <td>263</td>
      <td>282</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>439</td>
      <td>462</td>
      <td>283</td>
      <td>306</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>463</td>
      <td>477</td>
      <td>307</td>
      <td>321</td>
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

### Laterally open ligand-binding pocket of LPA6

The LPA6 structure reveals a unique laterally open ligand-binding pocket where a hydrophobic vertical cleft between TM4 and TM5 remains half-exposed to the lipid bilayer. This cleft accommodates the acyl chain of LPA, extending from the middle of the lipid bilayer. The central cavity includes aromatic and aliphatic residues creating a hydrophobic environment suitable for lipidic ligands. This "open" architecture differs from the sealed binding pockets of most class A GPCRs and allows LPA6 to laterally receive membrane-embedded LPA molecules produced by PA-PLA1alpha.

### Conserved positively charged residues recognize LPA phosphate

Five conserved positively charged residues (K26^1.31, R83^2.60, K188^5.32, R267^6.62, R281^7.32) are located at the periphery of the central cavity and mediate recognition of the negatively charged phosphate head group of LPA. Mutagenesis confirmed that K26^1.31, R83^2.60, R267^6.62 and R281^7.32 are critical for phosphate recognition, as alanine or glutamate mutations caused large reductions in receptor activity and LPA binding.

### TM6/TM7 inward shift mechanism for receptor activation

Docking simulations combined with mutagenesis suggest that LPA binding induces an inward shift of TM6 and TM7, bringing the positively charged residues on these helices (R267^6.62 and R281^7.32) into the central cavity to fully recognize the phosphate group. This inward shift mechanism is analogous to that observed in the evolutionarily related P2Y12 ADP receptor, where agonist binding induces TM6/TM7 closure. The motion of TM6 is crucial for coupling agonist binding to cytoplasmic G protein activation.

### Acyl chain binding and vertical cleft interactions

The acyl chain of LPA binds in the hydrophobic vertical cleft between TM4 and TM5, positioned between G157^4.56 and I198^5.42, with the chain terminus near L115^3.41, L153^4.52 and V201^5.45. Residues I198^5.42, V195^5.39, G157^4.56 and T161^4.60 are critical for acyl chain binding. LPA6 exhibits highest preference for LPA species with the linoleoyl (18:2) acyl chain. The synthetic potent agonist 2-alkyl-OMPT-(R), a stable analogue of 2-acyl LPA, was used for sensitive activity measurements.

### Structural similarity with P2Y family receptors

The LPA6 structure shows unexpected similarity to P2Y family ADP receptors. The pocket formed by TM3, TM4 and TM5 is a common structural feature among the P2Y family receptors and non-EDG family LPA receptors. In P2Y12, the adenine ring of ADP inserts into the same region as the LPA acyl chain in LPA6, indicating that both receptors use the same region to accommodate the "non-phosphate" moiety of their endogenous ligands. Other P2Y-related lipid receptors, such as lysophosphatidylserine receptors, may also use this pocket for acyl chain recognition.


## Cross-References

- <a href="/xray-mp-wiki/proteins/lpa1">Lysophosphatidic Acid Receptor 1 (LPA1)</a> — LPA1 is an EDG-family LPA receptor with distinct binding pocket architecture; sequenced and structurally compared
- <a href="/xray-mp-wiki/proteins/p2y12-receptor">P2Y12 Receptor</a> — Evolutionarily related P2Y family receptor sharing similar TM6/TM7 inward shift activation mechanism
