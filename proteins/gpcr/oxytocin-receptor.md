---
title: "Human Oxytocin Receptor (OTR)"
created: 2026-06-08
updated: 2026-06-29
type: protein
category: proteins
layout: default
tags: [gpcr, membrane-protein, xray-crystallography]
sources: [doi/10.1126##sciadv.abb5419]
verified: false
---

# Human Oxytocin Receptor (OTR)

## Overview

The human oxytocin receptor (OTR) is a class A G protein-coupled receptor (GPCR) that mediates the physiological effects of the neuropeptide hormone oxytocin, including regulation of parturition, lactation, and socioemotional behaviors. OTR belongs to the neurohypophyseal receptor family along with the vasopressin receptors (V1aR, V1bR, V2R). The receptor exhibits strong dependence on allosteric modulators including [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) and Mg2+ for proper function. The first crystal structure of OTR was determined in complex with the nonpeptidic antagonist [Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) at 3.2-A resolution using lipidic cubic phase (LCP) crystallization.


## Publications

### doi/10.1126##sciadv.abb5419

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
      <td><a class="pdb-link" href="https://www.rcsb.org/structure/6tpk">6TPK</a></td>
      <td>3.2</td>
      <td></td>
      <td>OTR_XTAL (PGS fusion, D153A/S224A, C-terminal <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a>)</td>
      <td><a href="/xray-mp-wiki/reagents/additives/retosiban/">Retosiban</a> (antagonist), <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a>, Mg2+ coordination site identified</td>
    </tr>
  </tbody>
</table>

**Expression:**

- **Expression system**: Spodoptera frugiperda (Sf9) insect cells
- **Construct**: OTR crystallization construct (OTR_XTAL) with PGS fusion in ICL3 (residues R232-L265 replaced), C-terminal [Protein Truncation for Crystallization](/xray-mp-wiki/concepts/methods-techniques/truncation/) (residues 360-389), and D153A/S224A thermostabilizing mutations
- **Notes**: SNAP tag and octahistidine affinity tag at N-terminus (removed by 3C protease and PNGase F after purification). Codon-optimized for Sf9.

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
      <td>Solubilization</td>
      <td>1% (w/v) <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a> + 0.2% (w/v) <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> in 30 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM KCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a></td>
      <td>—</td>
      <td>30 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM KCl, 5 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a></td>
      <td>Membranes solubilized for 2.5 h at 4 C with 100 uM <a href="/xray-mp-wiki/reagents/additives/retosiban/">Retosiban</a> and <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a></td>
    </tr>
    <tr>
      <td><a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> <a href="/xray-mp-wiki/methods/purification/immobilized-metal-affinity-chromatography/">IMAC</a> resin</td>
      <td>—</td>
      <td>Wash I: 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10 mM <a href="/xray-mp-wiki/reagents/additives/magnesium-chloride/">MgCl2</a>, 5 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 1% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.2% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 8 mM <a href="/xray-mp-wiki/reagents/ligands/atp/">ATP</a>, 50 uM <a href="/xray-mp-wiki/reagents/additives/retosiban/">Retosiban</a>. Wash II: 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 15 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 50 uM <a href="/xray-mp-wiki/reagents/additives/retosiban/">Retosiban</a></td>
      <td>Elution: 50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 250 mM <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.05% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.01% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 100 uM <a href="/xray-mp-wiki/reagents/additives/retosiban/">Retosiban</a></td>
    </tr>
    <tr>
      <td>Desalting / tag removal</td>
      <td>PD MiniTrap G-25 column</td>
      <td>—</td>
      <td>50 mM <a href="/xray-mp-wiki/reagents/buffers/hepes/">Hepes</a> pH 7.5, 500 mM <a href="/xray-mp-wiki/reagents/additives/sodium-chloride/">NaCl</a>, 10% <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a>, 0.03% <a href="/xray-mp-wiki/reagents/detergents/ddm/">DDM</a>, 0.006% <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a>, 100 uM <a href="/xray-mp-wiki/reagents/additives/retosiban/">Retosiban</a></td>
      <td><a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> removed, then treated with His-tagged 3C protease and PNGase F overnight to remove affinity tags and deglycosylate. Cleaved receptor collected as <a href="/xray-mp-wiki/reagents/additives/nickel-nta/">Ni-NTA</a> flow-through.</td>
    </tr>
    <tr>
      <td>Concentration</td>
      <td>100-kDa MWCO Vivaspin 2 concentrator</td>
      <td>—</td>
      <td>Same as G25 buffer</td>
      <td>Concentrated to ~70 mg/ml; typical yield ~0.8 mg per liter of expression volume</td>
    </tr>
  </tbody>
</table>

**Crystallization:**

<table class="wiki-kv-table">
  <tbody>
    <tr>
      <td>Method</td>
      <td>Lipidic cubic phase (<a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a>)</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>16</td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>OTR:<a href="/xray-mp-wiki/reagents/additives/retosiban/">Retosiban</a> complex (~70 mg/ml) mixed with molten <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> for <a href="/xray-mp-wiki/methods/crystallization/lipidic-cubic-phase/">LCP</a> reconstitution. Strong electron density for <a href="/xray-mp-wiki/reagents/additives/retosiban/">Retosiban</a>, <a href="/xray-mp-wiki/reagents/lipids/cholesterol/">Cholesterol</a>, and key interaction residues.</td>
    </tr>
  </tbody>
</table>
<div class="sequences" markdown="1">
**Sequences (PDBTM):**

<div class="sequence-entry" markdown="1">
**PDB <a class="pdb-link" href="https://www.rcsb.org/structure/6tpk">6TPK</a> — Chain A (7 TMs, alpha)**

<div class="sequence-display">
<div class="topo-legend">
<span class="topo-membrane-legend">&#9608; TM Helix</span>
<span class="topo-inside-legend">&#9608; Inside</span>
<span class="topo-outside-legend">&#9608; Outside</span>
<span class="topo-unknown-legend">&#9608; Unknown</span>
</div>
<div class="sequence-text">
<span class="topo-ruler">        10        20        30        40        50        60        70        80        90       100       110       120</span>
<span class="topo-line"><span class="topo-outside">NEA</span><span class="topo-membrane">LARVEVAVLCLILLLALSGNACVLL</span><span class="topo-inside">ALH</span><span class="topo-unknown">TTRQK</span><span class="topo-inside">HSRLFFF</span><span class="topo-membrane">MKHLSIADLVVAVFQVLPQLLWDI</span><span class="topo-outside">TFRFYG</span><span class="topo-membrane">PDLLCRLVKYLQLVGMFASTYLLLLMSL</span><span class="topo-inside">DRCLAICQPLRSLRRRTAR</span></span>
<span class="topo-ruler">       130       140       150       160       170       180       190       200       210       220       230       240</span>
<span class="topo-line"><span class="topo-inside">L</span><span class="topo-membrane">AVLATWLGCLVVSAPQVHIF</span><span class="topo-outside">SLREVADGVFDCWAVFIRPWG</span><span class="topo-membrane">PKAYITWITLAVYIVPVIVLATCYG</span><span class="topo-inside">LIAFKIWQN</span><span class="topo-unknown">LRLKTAAAAAAEAPEGAAAGDGGRVALARVSSVK</span><span class="topo-inside">LISKAKIRTV</span></span>
<span class="topo-ruler">       250       260       270       280       290       300       310       320       330       340       350       360</span>
<span class="topo-line"><span class="topo-inside">KM</span><span class="topo-membrane">TFIIVLAFIVCWTPFFFVQMWSVW</span><span class="topo-outside">DANAPKEA</span><span class="topo-membrane">SAFIIVMLLASLNCCCKPWIYML</span><span class="topo-inside">FMGHLFHGID?SFW</span><span class="topo-unknown">CC</span><span class="topo-inside">NESYLTGSRDERKKSLLSKFGMDEGVTFMFIGRFDRGQKGVDVLLKA</span></span>
<span class="topo-ruler">       370       380       390       400       410       420       430       440       450       460       470       480</span>
<span class="topo-line"><span class="topo-inside">IEILSSKKEFQEMRFIIIGKGDPELEGWARSLEEKHGNVKVITEMLSREFVRELYGSVDFVIIPSYFEPFGLVALEAMCLGAIPIASAVGGLRDIITNETGILVKAGDPGELANAILKAL</span></span>
<span class="topo-ruler">       490       500  </span>
<span class="topo-line"><span class="topo-inside">ELSRSDLSKFRENCKKRAMSFS</span></span>
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
      <td>3</td>
      <td>35</td>
      <td>37</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>4</td>
      <td>28</td>
      <td>38</td>
      <td>62</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>29</td>
      <td>31</td>
      <td>63</td>
      <td>65</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>37</td>
      <td>43</td>
      <td>71</td>
      <td>77</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>44</td>
      <td>67</td>
      <td>78</td>
      <td>101</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>68</td>
      <td>73</td>
      <td>102</td>
      <td>107</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>74</td>
      <td>101</td>
      <td>108</td>
      <td>135</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>102</td>
      <td>121</td>
      <td>136</td>
      <td>155</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>122</td>
      <td>141</td>
      <td>156</td>
      <td>175</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>142</td>
      <td>162</td>
      <td>176</td>
      <td>196</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>163</td>
      <td>187</td>
      <td>197</td>
      <td>221</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>188</td>
      <td>196</td>
      <td>222</td>
      <td>230</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>231</td>
      <td>242</td>
      <td>265</td>
      <td>276</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>243</td>
      <td>266</td>
      <td>277</td>
      <td>300</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>267</td>
      <td>274</td>
      <td>301</td>
      <td>308</td>
      <td>Outside</td>
    </tr>
    <tr>
      <td>275</td>
      <td>297</td>
      <td>309</td>
      <td>331</td>
      <td>Membrane</td>
    </tr>
    <tr>
      <td>298</td>
      <td>311</td>
      <td>332</td>
      <td>345</td>
      <td>Inside</td>
    </tr>
    <tr>
      <td>314</td>
      <td>502</td>
      <td>348</td>
      <td>536</td>
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

### Enlarged binding pocket

The OTR binding pocket is approximately 25% larger than other non-peptide antagonist-bound neuropeptide GPCRs and ~50% larger than the agonist-bound NTS1R. The enlarged pocket likely accommodates the cyclic nonapeptide agonist oxytocin.

### Retosiban binding mode

[Retosiban](/xray-mp-wiki/reagents/additives/retosiban/) adopts an upright, elongated conformation in the binding pocket with its 2,5-diketopiperazine (DKP) core. The binding interface features a polar hemisphere (helices II-IV, residues Q119, Q171, K116) and a hydrophobic hemisphere (helices V-VII). Key polar interactions include hydrogen bonds between Q171^4.60 and the DKP 2-keto oxygen, and between Q119^3.32 and the DKP N1.

### Extrahelical cholesterol binding site

A [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) molecule binds in a previously undescribed extrahelical location between helices IV and V, capped by ECL2. Key interactions involve Y200^5.38 and W203^5.41 on helix V, and P170^4.59, I174^4.63, and ECL2 residues. [Cholesterol](/xray-mp-wiki/reagents/lipids/cholesterol/) binding stabilizes the receptor through direct contact with ECL2 and by orienting Y200^5.38 to form a hydrogen bond with Q171^4.60, thereby coordinating the polar network of the binding pocket.

### Divalent cation coordination site

Two acidic residues, E42^1.35 and D100^2.65, at the extracellular tips of helices I and II form a highly conserved Mg2+ binding site. Mg2+ acts as a positive allosteric modulator for agonist binding. This represents the first identification of a distinct, solvent-exposed divalent cation coordination site in a GPCR.


## Cross-References

- <a href="/xray-mp-wiki/reagents/lipids/monoolein/">Monoolein</a> — Used as the LCP matrix for OTR crystallization
- <a href="/xray-mp-wiki/concepts/signaling-receptors/gpcr-active-state-high-affinity-agonist-binding/">GPCR Active State and High-Affinity Agonist Binding</a> — OTR is a class A GPCR with allosteric modulation by cholesterol and Mg2+
- <a href="/xray-mp-wiki/concepts/methods-techniques/truncation/">Protein Truncation for Crystallization</a> — Related biological concept
- <a href="/xray-mp-wiki/methods/purification/affinity-chromatography/">Affinity Chromatography</a> — Method used in structure determination or purification
- <a href="/xray-mp-wiki/reagents/detergents/cholesterol-hydrogen-succinate/">CHS</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/glycerol/">Glycerol</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/imidazole/">Imidazole</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/iodoacetamide/">Iodoacetamide</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/retosiban/">Retosiban</a> — Additive used in purification or crystallization buffers
- <a href="/xray-mp-wiki/reagents/additives/talon/">TALON</a> — Additive used in purification or crystallization buffers
